/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {

    public TreeNode invert(TreeNode temp)
    {
        if(temp==null)
        {
            return null;
        }
         TreeNode left = invert(temp.left);
         TreeNode right = invert(temp.right); 
         temp.right=left;
         temp.left=right;

         return temp;
    }

    public TreeNode invertTree(TreeNode root) {
        return invert(root);
        }
    }

