#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * insert_node - inserts a number into a sorted linked list
 * @head: address of head pointer
 * @number: number to be insetred at node
 *
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *min = *head;
	listint_t *max = *head;
	listint_t *tmp = *head;
	listint_t *new;

	new = malloc(sizeof(listint_t) * 1);
	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		*head->next = new;
		return (new);
	}

	while (min->next != NULL)
	{
		max = max->next;
		if (number > min->n && number < max->n)
		{
			min->next = new;
			new->next = max;
			return (new);
		}
		if (number < min->n)
		{
			temp->next = new;
			new->next = min;
		}

		min = min->next;
	}
	return (NULL);
}
