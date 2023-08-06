#![feature(proc_macro_hygiene, decl_macro)]
extern crate deunicode;
extern crate pest;
#[macro_use]
extern crate pest_derive;

use pyo3::prelude::*;

mod parser;
mod types;

#[pyfunction]
fn dostuff() -> PyResult<types::ParsedRobotsTxt> {
    let result = parser::parse("user-agent: googlebot\nallow: *\n".to_string()).unwrap();
    println!("{:#?}",result);
    return Ok(result);
}

#[pyfunction]
fn parse(s: String) -> PyResult<types::ParsedRobotsTxt>  {
    let result = parser::parse(s).unwrap();
    return Ok(result);
}


#[pyfunction]
fn diff_rules(l: types::CollatedRules, r: types::CollatedRules) -> PyResult<types::DiffedRules>  {
    let result = types::diff_rules(l,r);
    return Ok(result);
}


#[pyfunction]
fn is_probably_parseable(s: String) -> PyResult<bool> {
    return Ok(parser::is_probably_parseable(s))
}

/// A Python module implemented in Rust. The name of this function must match
/// the `lib.name` setting in the `Cargo.toml`, else Python will not be able to
/// import the module.
#[pymodule]
fn rbdt(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(dostuff, m)?)?;
    m.add_function(wrap_pyfunction!(parse,m)?)?;
    m.add_function(wrap_pyfunction!(diff_rules,m)?)?;
    m.add_function(wrap_pyfunction!(is_probably_parseable,m)?)?;
    m.add_class::<types::CollatedRules>()?;
    Ok(())
}