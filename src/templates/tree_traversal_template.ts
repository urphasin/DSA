import { TreeNode } from "@structures/TreeNode";

// Recursive DFS
function dfsRecursive(node: TreeNode | null): void {
  if (!node) return;
  // process node
  console.log(node.val);
  dfsRecursive(node.left);
  dfsRecursive(node.right);
}

// Iterative DFS
function dfsIterative(root: TreeNode | null): void {
  const stack: TreeNode[] = [];
  if (root) stack.push(root);

  while (stack.length > 0) {
    const node = stack.pop()!;
    console.log(node.val);
    if (node.right) stack.push(node.right);
    if (node.left) stack.push(node.left);
  }
}

// BFS
function bfs(root: TreeNode | null): void {
  const queue: TreeNode[] = [];
  if (root) queue.push(root);

  while (queue.length > 0) {
    const node = queue.shift()!;
    console.log(node.val);
    if (node.left) queue.push(node.left);
    if (node.right) queue.push(node.right);
  }
}

export { dfsRecursive, dfsIterative, bfs };