# Time Complexity of Array Operations

| Operation           | Time Complexity | Explanation                       |
|---------------------|-----------------|---------------------------------|
| Access (by index)   | O(1)            | Direct access via index          |
| Search (unsorted)   | O(n)            | Linear scan through elements     |
| Search (sorted)     | O(log n)        | Binary search                   |
| Insertion (end)     | O(1) amortized  | Append element at the end        |
| Insertion (middle)  | O(n)            | Shift elements to make space     |
| Deletion (end)      | O(1)            | Remove last element              |
| Deletion (middle)   | O(n)            | Shift elements to fill gap       |
| Resize (dynamic)    | O(n)            | Copy elements to new array       |

