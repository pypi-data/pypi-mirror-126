use itertools::Itertools;
use pyo3::prelude::*;
use regex::Regex;
use std::cmp::Ordering;
use std::collections::HashSet;
use pyo3::PyObjectProtocol;
use pyo3::basic::CompareOp;

#[pyclass]
#[derive(Debug, Clone, Default, PartialEq)]
pub struct CollatedRules {
    #[pyo3(get)]
    pub user_agents: HashSet<String>,
    #[pyo3(get)]
    pub allows: HashSet<String>,
    #[pyo3(get)]
    pub disallows: HashSet<String>,
}


#[pymethods]
impl CollatedRules {
    #[new]
    fn new(user_agents: HashSet<String>, allows: HashSet<String>, disallows: HashSet<String>) -> Self {
        CollatedRules{user_agents, allows, disallows} 
    }
}

#[pyproto]
impl PyObjectProtocol for CollatedRules {
    fn __str__(&self) -> PyResult<String>   {
        Ok(format!("{:#?}", self))
    }

    fn __repr__(&self) -> PyResult<String> {
        Ok(format!("{:#?}", self))
    }

    fn __richcmp__(&self, other: PyRef<CollatedRules>, op: CompareOp) -> Py<PyAny> {
        let py = other.py();
        match op {
            CompareOp::Eq => {

                (self.user_agents == other.user_agents && self.disallows == other.disallows && self.allows == other.allows).into_py(py)
            }
            _ =>  {
            py.NotImplemented()
            }
        }
    }
}

pub type ParsedRobotsTxt = std::vec::Vec<CollatedRules>;

pub fn is_totally_blocked(block: &CollatedRules) -> bool {
    block.disallows.len() == 1 && block.disallows.contains("/") && block.allows.is_empty()
}

pub fn is_totally_open(block: &CollatedRules) -> bool {
    (block.allows.len() == 1 && block.allows.contains("/") && block.disallows.is_empty())
        || (block.disallows.len() == 1 && block.disallows.contains("") && block.allows.is_empty())
}

#[pyclass]
#[derive(Debug, Clone, Default, PartialEq)]
pub struct DiffedRules {
    #[pyo3(get)]
    pub extra_allows: Vec<String>,
    #[pyo3(get)]
    pub missing_allows: Vec<String>,
    #[pyo3(get)]
    pub mutal_allows: Vec<String>,
    #[pyo3(get)]
    pub extra_disallows: Vec<String>,
    #[pyo3(get)]
    pub missing_disallows: Vec<String>,
    #[pyo3(get)]
    pub mutal_disallows: Vec<String>,
}

pub fn diff_rules(left: CollatedRules, right: CollatedRules) -> DiffedRules {
    let extra_allows: Vec<String> = left
        .allows
        .difference(&right.allows)
        .into_iter()
        .sorted()
        .filter(|s| !s.is_empty())
        .map(|s| s.to_string())
        .collect();

    let missing_allows: Vec<String> = right
        .allows
        .difference(&left.allows)
        .into_iter()
        .sorted()
        .filter(|s| !s.is_empty())
        .map(|s| s.to_string())
        .collect();

    let mutal_allows: Vec<String> = right
        .allows
        .intersection(&left.allows)
        .into_iter()
        .sorted()
        .filter(|s| !s.is_empty())
        .map(|s| s.to_string())
        .collect();

    let extra_disallows: Vec<String> = left
        .disallows
        .difference(&right.disallows)
        .into_iter()
        .sorted()
        .filter(|s| !s.is_empty())
        .map(|s| s.to_string())
        .collect();

    let missing_disallows: Vec<String> = right
        .clone()
        .disallows
        .difference(&left.disallows)
        .into_iter()
        .sorted()
        .filter(|s| !s.is_empty())
        .map(|s| s.to_string())
        .collect();

    let mutal_disallows: Vec<String> = right
        .clone()
        .disallows
        .intersection(&left.disallows)
        .into_iter()
        .sorted()
        .filter(|s| !s.is_empty())
        .map(|s| s.to_string())
        .collect();

    return DiffedRules{
        extra_allows,
        missing_allows,
        mutal_allows,
        extra_disallows,
        missing_disallows,
        mutal_disallows,
    };
}

fn convert_url_to_regex(mut s: String) -> Regex {
    s = s.replace("*", ".*");
    for i in vec!["?", "(", ")", "[", "]", "{", "}", "^", "|", "+"] {
        s = s.replace(i, format!("\\{}", i).as_str());
    }
    s += ".*$";
    s = "^".to_string() + &s;
    // where to escape?
    Regex::new(&s).unwrap()
}

fn diff_rules_2(
    left: HashSet<String>,
    right: HashSet<String>,
) -> (HashSet<String>, HashSet<String>) {
    let mut leftovers = left.clone();
    let mut rightovers = right.clone();

    let left_regexes: Vec<Regex> = left
        .iter()
        .map(|x| convert_url_to_regex(x.to_string()))
        .collect();
    let right_regexes: Vec<Regex> = right
        .iter()
        .map(|x| convert_url_to_regex(x.to_string()))
        .collect();

    /*     println!("left regexes: {:#?}", left_regexes);
    println!("right regexes: {:#?}", right_regexes);

    println!("Before:");
    println!("leftovers: {:#?}", leftovers);
    println!("rightovers: {:#?}", rightovers); */
    leftovers.retain(|x| !right_regexes.iter().any(|r| r.is_match(&x)));
    rightovers.retain(|x| !left_regexes.iter().any(|r| r.is_match(&x)));
    /*     println!("After:");
    println!("leftovers: {:#?}", leftovers);
    println!("rightovers: {:#?}", rightovers);
    println!(""); */

    return (leftovers, rightovers);
}

fn can_access(r: CollatedRules, s: String) -> bool {
    let matching_allow: Option<usize> = r
        .allows
        .iter()
        .map(|x| convert_url_to_regex(x.to_string()))
        .filter(|r| r.is_match(&s))
        .map(|r| r.as_str().to_string().len())
        .max();
    let matching_disallow: Option<usize> = r
        .disallows
        .iter()
        .map(|x| convert_url_to_regex(x.to_string()))
        .filter(|r| r.is_match(&s))
        .map(|r| r.as_str().to_string().len())
        .max();
    let result = match (matching_allow, matching_disallow) {
        (None, None) => true,
        (Some(_), None) => true,
        (None, Some(_)) => false,
        (Some(i), Some(j)) => i > j,
    };
    return result;
}

fn partial_cmp_urlsets(left: HashSet<String>, right: HashSet<String>) -> Option<Ordering> {
    let (leftovers, rightovers) = diff_rules_2(left, right);

    //println!("leftovers: {:#?}", leftovers);
    //println!("rightovers: {:#?}", rightovers);

    let result = match (leftovers.len(), rightovers.len()) {
        (0, 0) => Some(Ordering::Equal),
        (i, 0) if i > 0 => Some(Ordering::Greater),
        (0, i) if i > 0 => Some(Ordering::Less),
        (i, j) if i > 0 && j > 0 => None,
        (_, _) => panic!("oh no"),
    };
    //println!("partial_cmp_urlsets: {:#?}", result);
    return result;
}

pub fn rough_cmp_rules(left: &CollatedRules, right: &CollatedRules) -> Option<Ordering> {
    // if one is clearly better, than return that because it is also roughly better as well
    let strict_cmp = left.partial_cmp(right);
    if strict_cmp.is_some() {
        return strict_cmp;
    }

    let (allow_leftovers, allow_rightovers) =
        diff_rules_2(left.clone().allows, right.clone().allows);
    let (disallow_leftovers, disallow_rightovers) =
        diff_rules_2(left.clone().disallows, right.clone().disallows);

    let mut left_score = allow_leftovers.len() as i64 - disallow_leftovers.len() as i64;
    let mut right_score = allow_rightovers.len() as i64 - disallow_rightovers.len() as i64;

    if left.disallows.contains("/") {
        left_score -= 100;
    }

    if left.allows.contains("/") {
        left_score += 100;
    }

    if right.disallows.contains("/") {
        right_score -= 100;
    }

    if right.allows.contains("/") {
        right_score += 100;
    }

    // contains a star worth more?
    //make this score the whole thing in total, seperately than compare?
    return match left_score - right_score {
        n if n >= 5 => Some(Ordering::Greater),
        n if n <= -5 => Some(Ordering::Less),
        _ => None,
    };
}

impl PartialOrd for CollatedRules {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        if is_totally_blocked(self) && !is_totally_blocked(other) {
            return Some(Ordering::Less);
        }

        if !is_totally_blocked(self) && is_totally_blocked(other) {
            return Some(Ordering::Greater);
        }

        if is_totally_open(self) && !is_totally_open(other) {
            return Some(Ordering::Greater);
        }

        if !is_totally_open(self) && is_totally_open(other) {
            return Some(Ordering::Less);
        }

        //prefix and star
        let r = match (
            partial_cmp_urlsets(self.clone().allows, other.clone().allows),
            partial_cmp_urlsets(self.clone().disallows, other.clone().disallows),
        ) {
            (None, _) => None,
            (_, None) => None,

            //One has more allows, while having more disallows, can't say anything
            (Some(Ordering::Less), Some(Ordering::Less)) => None,
            (Some(Ordering::Greater), Some(Ordering::Greater)) => None,

            (Some(Ordering::Equal), Some(Ordering::Equal)) => Some(Ordering::Equal),

            (Some(Ordering::Equal), Some(Ordering::Greater)) => Some(Ordering::Less),
            (Some(Ordering::Less), Some(Ordering::Equal)) => Some(Ordering::Less),
            (Some(Ordering::Less), Some(Ordering::Greater)) => Some(Ordering::Less),

            (Some(Ordering::Greater), Some(Ordering::Equal)) => Some(Ordering::Greater),
            (Some(Ordering::Equal), Some(Ordering::Less)) => Some(Ordering::Greater),
            (Some(Ordering::Greater), Some(Ordering::Less)) => Some(Ordering::Greater),
        };
        //println!("partial_cmp result: {:#?}", r);
        return r;
    }
}

/* impl PartialEq for CollatedRules {
    fn eq(&self, other: &Self) -> bool {
        self.partial_cmp(other) == Some(Ordering::Equal)
    }
} */
