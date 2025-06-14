pub(crate) fn main() {
  let nums = [10, 20, 30, 40, 50];

  println!("First element: {}", nums[0]);
  println!("Array len: {}", nums.len());

  for (i, val) in nums.iter().enumerate() {
    println!("Index {}: {}", i, val);
  }
}