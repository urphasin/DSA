use std::collections::HashMap;

pub(crate) fn main() {
  let nums = vec!{1, 2, 7, 11, 15};
  let target = 9;

  if let Some((i, j)) = two_sum(&nums, target) {
    println!("Indices: ({}, {})", i, j);
  } else {
      println!("No solutions found");
  }
}

fn two_sum(nums: &[i32], target: i32) -> Option<(usize, usize)> {
  let mut map = HashMap::new();

  for (i, &num) in nums.iter().enumerate() {
      let complement = target - num;
      if let Some(&j) = map.get(&complement) {
        return Some((j, i));
      }
      map.insert(num, i);
  }

  None
}