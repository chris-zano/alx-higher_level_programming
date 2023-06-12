#include "lists.h"

/**
 * is_palindrome - checks to see if a linked list is a palindrome
 * @head: pointer to the head of the linked list
 * Return: 0 (not palindrome), 1 (palindrome)
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *curr = *head;
	listint_t *prev = NULL, *next = NULL;
	int isTrue = 1;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		next = slow->next;
		slow->next = prev;
		prev = slow;
		slow = next;
	}

	if (fast != NULL)
		slow = slow->next;

	while (prev != NULL)
	{
		if (prev->n != slow->n)
		{
			isTrue = 0;
			break;
		}
		prev = prev->next;
		slow = slow->next;
	}
	prev = NULL;
	while (curr != NULL)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}
	*head = prev;
	return (isTrue);
}
