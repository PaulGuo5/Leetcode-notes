/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* prev;
    Node* next;
    Node* child;
};
*/

class Solution {
public:
    Node* flatten(Node* head) {
        if (!head) return head;
        
        for(Node* h=head; h; h = h->next) {
            if(h->child) {
                Node* nxt = h->next;
                h->next = h->child;
                h->child = NULL;
                h->next->prev = h;
                Node* p = h->next;
                while(p->next) p = p->next;
                p->next = nxt;
                if (nxt) nxt->prev = p;
            }
        }
        return head;
    }
};
