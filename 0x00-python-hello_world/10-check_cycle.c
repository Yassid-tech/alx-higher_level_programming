#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @head: A pointer to the head of the singly-linked list.
 *
 * Return: 1 if there is a cycle, 0 otherwise.
 */
int check_cycle(listint_t *head)
{
if (head == NULL || head->next == NULL)
return 0;
listint_t *slow_ptr = head;
listint_t *fast_ptr = head->next;
while (slow_ptr && fast_ptr && fast_ptr->next)
{
if (slow_ptr == fast_ptr)
return 1;
slow_ptr = slow_ptr->next;
fast_ptr = fast_ptr->next->next;
}
return 0;
}
