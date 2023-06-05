#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * check_cycle - checks if a linked lists has a cycle in it
 * @list: pointer to head node of the linked list
 * Return: 0 if there is no cycle,
 * 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *tmp = list;
	listint_t *hare = list;

	if (hare == NULL)
		return (0);
	if (hare->next == NULL || hare->next->next == NULL)
		return (0);

	while (hare != NULL && hare->next != NULL)
	{
		hare = hare->next->next;
		tmp = tmp->next;
		if (tmp == hare)
			return (1);
	}
	return (0);
}
