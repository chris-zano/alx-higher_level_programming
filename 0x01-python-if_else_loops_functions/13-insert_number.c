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
	listint_t *min = NULL;
	listint_t *max = *head;
	listint_t *new;

	new = malloc(sizeof(listint_t) * 1);
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next =  NULL;

	if (*head == NULL || number <= max->n)
	{
		new->next = max;
		*head = new;
		return (new);
	}

	while (max != NULL && number > max->n)
	{
		min = max;
		max = max->next;
	}

	min->next = new;
	new->next = max;


	return (new);
}
