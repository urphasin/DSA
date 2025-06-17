# Tree Mastery Roadmap

🧠 **Phase 1: Foundations — Learn the Concepts**

1. **Understand the Basics**
   * What is a binary tree?
   * What is a binary search tree?
   * Tree traversal (DFS: in-order, pre-order, post-order; BFS: level-order)
   * Height, depth, diameter, leaf, balanced/unbalanced trees

2. **Implement from Scratch in TypeScript** Practice by writing:

```typescript
class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
  
  constructor(val: number, left: TreeNode | null = null, right: TreeNode | null = null) {
    this.val = val;
    this.left = left;
    this.right = right;
  }
}
```

🧩 **Phase 2: LeetCode Easy — Hands-On Traversals & Basics**

Start here:
* 94. Binary Tree Inorder Traversal
* 144. Binary Tree Preorder Traversal
* 145. Binary Tree Postorder Traversal
* 102. Binary Tree Level Order Traversal
* 101. Symmetric Tree
* 100. Same Tree
* 104. Maximum Depth of Binary Tree
* 110. Balanced Binary Tree

👉 Each time, **manually trace** your traversal with pen and paper or console logs.
👉 Try both recursive and iterative solutions.

🔧 **Phase 3: LeetCode Medium — Recursion + Tree Properties**

Move to these:
* 105. Construct Binary Tree from Preorder and Inorder
* 106. Construct Binary Tree from Inorder and Postorder
* 124. Binary Tree Maximum Path Sum
* 236. Lowest Common Ancestor of a Binary Tree
* 230. Kth Smallest Element in a BST
* 98. Validate Binary Search Tree
* 199. Binary Tree Right Side View

👉 Ask yourself:
* Can I write the recursive signature before diving in?
* Can I visualize the subtrees and return types?

🔥 **Phase 4: LeetCode Hard — Complex Recursion, States, DP on Trees**

Try these:
* 968. Binary Tree Cameras
* 297. Serialize and Deserialize Binary Tree
* 1245. Tree Diameter
* 742. Closest Leaf in a Binary Tree
* 312. Burst Balloons (tree-based dynamic programming)

👉 Keep a **decision tree** of what each recursive call is trying to achieve.
👉 Write out the **state you're passing** (node, depth, sum, etc.).

🧗 **Phase 5: Codeforces & Advanced Tree Thinking**

These contests often twist trees in clever ways (e.g., graph disguised as a tree):
* Practice at: Codeforces Tree Tag
* Focus on:
   * **DFS numbering**
   * **Euler Tour**
   * **Lowest Common Ancestor (LCA)** via binary lifting
   * **Heavy-Light Decomposition** (when you're feeling confident)

Start with:
* Codeforces 1141F2 – Same Sum Blocks (involves subtree ideas)
* Codeforces 1006E – Military Problem (Euler tour simulation)
* Codeforces 1324E – Sleeping Schedule (tree DP)
* Codeforces 1304D – Shortest and Longest LIS (you'll notice patterns)

📘 **Notes System to Build**

As you solve:
* Write `.md` files with:
   * Problem name, link
   * What the recursion is doing
   * Key edge cases you hit
   * If iterative or recursive was easier

## Next Steps

Would you like me to give you:
1. A script you can use as a **TreeNode template** in TypeScript?
2. A starter exercise today to test your current understanding?

Let me know!