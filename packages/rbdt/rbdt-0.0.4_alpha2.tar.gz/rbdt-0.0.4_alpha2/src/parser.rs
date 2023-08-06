use crate::types::CollatedRules;

use itertools::Itertools;
use pest::Parser;
use std::collections::HashSet;
use regex;
#[derive(Parser)]
#[grammar = "robots.txt.pest"]
pub struct RobotsDotTxtParser;
use unicode_bom::Bom;
use deunicode::deunicode;

fn remove_bom(contents: String) -> String {
    let bom: Bom = Bom::from(contents.as_bytes());
    match bom {
        Bom::Null => {
            contents
        },
        Bom::Utf8 => {
            contents[3..].to_string()
        }
        _ => panic!("Unrecognized bom: {:#?}", bom) 
    }
}

pub fn is_probably_parseable(contents: String) -> bool {
    contents.to_lowercase().contains("user-agent")
}

pub fn parse(mut contents: String) -> Result<Vec<CollatedRules>, Box<dyn std::error::Error>> {
    contents = contents.trim().to_string();
    contents = remove_bom(contents);
    contents = deunicode(&contents);
    contents = contents.lines().map(|l| l.trim()).join("\n");
    contents = contents.lines().filter(|l| !l.starts_with("#")).join("\n");
    contents = contents.lines().filter(|l| !l.starts_with("<!--")).join("\n");
    contents = contents.lines().filter(|l| !l.starts_with("Updated")).join("\n");
    contents = contents.lines().map(|l| l.split("#").collect::<Vec<&str>>()[0]).join("\n");
    contents = contents.lines().map(|l| l.trim()).join("\n");
    contents = regex::Regex::new(r"\n+").unwrap().replace_all(&contents,"\n").to_string();
    contents = regex::Regex::new(r"User_agent").unwrap().replace_all(&contents,"User-agent").to_string();
    contents = regex::Regex::new(r"Dissalow").unwrap().replace_all(&contents,"Disallow").to_string();


    //how to skip this?
    contents.push('\n');

    let mut parsed = RobotsDotTxtParser::parse(Rule::file, &contents)?;

    let blocks = parsed
        .next()
        .unwrap()
        .into_inner()
        .filter(|pair| pair.as_rule() == Rule::block)
        .map(|pair| {
            let contents = pair.into_inner();

            let user_agents: HashSet<String> = contents
                .clone()
                .filter(|pair| pair.as_rule() == Rule::user_agent)
                .map(|pair| {
                    if let Some(v) = pair.into_inner().next() {
                        v
                        .as_str()
                        .to_string()
                        .to_lowercase()

                    }
                    else {
                        "EMPTY_USERAGENT_MARKER".to_string()
                    }
                })
                .collect();

            let disallows: HashSet<String> = contents
                .clone()
                .filter(|pair| pair.as_rule() == Rule::disallow)
                .map(|pair| pair.into_inner().next().unwrap().as_str().to_string())
                .collect();

            let allows: HashSet<String> = contents
                .clone()
                .filter(|pair| pair.as_rule() == Rule::allow)
                .map(|pair| pair.into_inner().next().unwrap().as_str().to_string())
                .collect();

            CollatedRules {
                user_agents,
                allows,
                disallows,
            }
        });

    // Merge blocks based on user agent
    let grouped = blocks
        .into_iter()
        .map(|block| {
            (
                block
                    .user_agents
                    .clone()
                    .into_iter()
                    .collect::<Vec<String>>(),
                block,
            )
        })
        .into_group_map();

    let merged = grouped
        .values()
        .map(|blocks| {
            blocks
                .iter()
                .fold(CollatedRules::default(), |mut acc, x| {
                    acc.user_agents
                        .extend(&mut x.clone().user_agents.into_iter());
                    acc.allows.extend(&mut x.clone().allows.into_iter());
                    acc.disallows.extend(&mut x.clone().disallows.into_iter());
                    acc
                })
        })
        .collect::<Vec<CollatedRules>>();

    // Merge blocks based on rules
    let grouped = merged
        .into_iter()
        .map(|block| {
            let mut allows = block.allows.clone().into_iter().collect::<Vec<String>>();
            let mut disallows = block.disallows.clone().into_iter().collect::<Vec<String>>();
            allows.sort();
            disallows.sort();
            ((allows, disallows), block)
        })
        .into_group_map();

    let merged = grouped
        .values()
        .map(|blocks| {
            blocks
                .iter()
                .fold(CollatedRules::default(), |mut acc, x| {
                    acc.user_agents
                        .extend(&mut x.clone().user_agents.into_iter());
                    acc.allows.extend(&mut x.clone().allows.into_iter());
                    acc.disallows.extend(&mut x.clone().disallows.into_iter());
                    acc
                })
        })
        .collect::<Vec<CollatedRules>>();

    Ok(merged)
}

// TODO assuming https???
// TODO look up how store steampowered/com is parsed 