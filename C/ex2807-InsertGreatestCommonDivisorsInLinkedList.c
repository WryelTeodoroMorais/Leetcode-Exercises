/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

 struct ListNode* insertGreatestCommonDivisors(struct ListNode* head) 
{
    struct ListNode* atual = head;
    while (atual != NULL && atual->next != NULL) 
    {
        int valor_atual = atual->val;
        int valor_proximo = atual->next->val;
        while (valor_proximo != 0) 
        {
            int temp = valor_proximo;
            valor_proximo = valor_atual % valor_proximo;
            valor_atual = temp;
        }
        
        struct ListNode* novo_no = (struct ListNode*)malloc(sizeof(struct ListNode));
        novo_no->val = valor_atual;
        novo_no->next = atual->next;
        atual->next = novo_no;
        atual = novo_no->next;
    }

    return head;
}