#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - insert node in a sorted linked list
 * @head: head of the linked list
 * @number: user input/node
 * Return: address of the node or NULL
 *
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	} else
	{
		while (node && node->next && node->next->n < number)
			node = node->next;
		new->next = node->next;
		node->next = new;
		return (new);
	}
	return (0);
}
