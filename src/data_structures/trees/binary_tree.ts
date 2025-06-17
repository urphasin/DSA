class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;

  constructor(val: number) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

function inOrder(node: TreeNode | null): void {
  if (!node) return;
  inOrder(node.left);
  console.log(node.val);
  inOrder(node.right);
}

// test
const root = new TreeNode(1);
root.left = new TreeNode(2);
root.right = new TreeNode(3);
inOrder(root);
