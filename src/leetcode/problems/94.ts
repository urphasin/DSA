// Binary Tree Inorder Traversal
import { TreeNode } from "@structures/TreeNode";

function inorderTreeTraversal(root: TreeNode | null): number[] {
  let res: number[] = [];

    (function traverse(node) {
        if (node === null) return;
        traverse(node.left);
        res.push(node.val);
        traverse(node.right);
    })(root);

  return res;
}