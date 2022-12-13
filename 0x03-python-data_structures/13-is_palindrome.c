#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a list has a cycle/ a palindrome
 * @head: pointer to the head of the node
 * Return: 0 if it is not a palindrome, 1 if it is
 *
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev = NULL;
	listint_t *next;
	int res = 1;

	if (*head == NULL)
		return (1);

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

	while (slow != NULL)
	{
		if (slow->n != prev->n)
			res = 0;
		slow = slow->next;
		prev = prev->next;
	}
	return (res);
}
