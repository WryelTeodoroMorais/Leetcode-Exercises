
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

 struct ListNode* mergeNodes(struct ListNode* head) 
{
    struct ListNode* atual = head;
    struct ListNode* head_new = NULL;
    struct ListNode* tail = NULL;

    while(atual->next != NULL)
    {
        int temp = 0;
        while(atual->next->val != 0)
        {
            atual=atual->next;
            temp+=atual->val;
        }

        struct ListNode* new_no = (struct ListNode*) malloc (sizeof(struct ListNode));

        atual = atual->next;
        new_no->val = temp;
        new_no->next = NULL;

        if (head_new == NULL)
        {
            head_new = new_no;
            tail = new_no;
        }
        else
        {
            tail->next = new_no;
            tail = new_no;
        }
    }

    free(head);
    return head_new;
}