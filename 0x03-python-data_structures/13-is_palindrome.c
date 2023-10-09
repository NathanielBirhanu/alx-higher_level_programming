#include "lists.h"
/**
 * is_palindrome - Checks if a linked list is a palindrome.
 * @head: A double pointer to the head of the linked list.
 *
 * Return: 1 if the linked list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head;
    listint_t *fast = *head;

    while (fast && fast->next)
    {
        slow = slow->next;
        fast = fast->next->next;
    }
    listint_t *prev = NULL;
    while (slow)
    {
        listint_t *next_node = slow->next;
        slow->next = prev;
        prev = slow;
        slow = next_node;
    }

    listint_t *first_half = *head;
    listint_t *second_half = prev;
    while (first_half && second_half)
    {
        if (first_half->val != second_half->val)
            return 0;

        first_half = first_half->next;
        second_half = second_half->next;
    }

    return 1;
}
