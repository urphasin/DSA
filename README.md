# 🧠 My Honest Promise to You

You **will enjoy coding** more in Rust from this point on than C++. You'll get more done. You'll feel safer. And you'll spend more time thinking about **problems**, not the toolchain.

Would you like a fast cheat sheet for common Rust patterns for DSA (like `Vec`, `HashMap`, etc.) to get you rolling faster than you ever did with C++?

---

# 🧠 Rust DSA Cheat Sheet

## 📦 Common Imports

```rust
use std::collections::{HashMap, HashSet, VecDeque, BinaryHeap};
```

## 🧰 Arrays and Vectors

```rust
let arr = [1, 2, 3];        // fixed size array
let mut vec = vec![1, 2, 3]; // growable vector
vec.push(4);
vec.pop();
vec.len();
vec.sort();
```

**Loop:**

```rust
for x in &vec {
    println!("{}", x);
}

for (i, val) in vec.iter().enumerate() {
    println!("Index {}: {}", i, val);
}
```

## 📚 Strings

```rust
let s = String::from("hello");
let slice = &s[0..2];  // substring
let chars: Vec<char> = s.chars().collect();
```

**Mutable:**

```rust
let mut s = String::new();
s.push('a');
s.push_str("bc");
```

## 🧮 HashMap / HashSet

```rust
let mut map = HashMap::new();
map.insert("a", 1);
map.get("a");  // Option<&i32>

let mut set = HashSet::new();
set.insert(1);
set.contains(&1);
```

## 🌀 Queues & Stacks

**`VecDeque` = Queue**

```rust
let mut q = VecDeque::new();
q.push_back(1);  // enqueue
q.pop_front();   // dequeue
```

**`Vec` = Stack**

```rust
let mut stack = vec![];
stack.push(10);
stack.pop();
```

## 🔢 Binary Heap (Max by default)

```rust
let mut heap = BinaryHeap::new();
heap.push(10);
heap.push(2);
heap.pop();  // gives max
```

**To get a min-heap:**

```rust
use std::cmp::Reverse;

let mut min_heap = BinaryHeap::new();
min_heap.push(Reverse(5));
min_heap.push(Reverse(1));
min_heap.pop().unwrap().0;
```

## ⚙️ Loops & Conditions

```rust
for i in 0..n {  // 0 to n-1
}

while let Some(val) = vec.pop() {
    // loop while popping
}

if let Some(v) = map.get("key") {
    println!("{}", v);
}
```

## 📎 Pattern Matching

```rust
match some_val {
    Some(x) => println!("Got {}", x),
    None => println!("Nothing"),
}
```

## 💡 Utility Helpers

```rust
vec.iter().sum::<i32>();
vec.iter().max();
vec.clone();    // deep copy
vec.reverse();
```

## ✍️ Writing Fast Input Templates (Optional)

```rust
use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let mut lines = stdin.lock().lines();
    
    let first = lines.next().unwrap().unwrap();  // Read first line
    let nums: Vec<i32> = first
        .split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
}
```

## 🏁 TL;DR DSA Crates Worth Knowing

| Crate | Use |
|-------|-----|
| `itertools` | Slicing, grouping, combos |
| `rand` | Randomized algorithms |
| `proconio` | Fast input for CP |
| `regex` | Pattern matching |