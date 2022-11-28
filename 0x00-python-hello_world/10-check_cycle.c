#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - cycle or loop function
 * @list: listint_t list
 * Return: 0 if there is a cycle, 1 if no cycle
 *
 */

int check_cycle(listint_t *list)
{
	listint_t *fast_ptr = list;
	listint_t *slow_ptr = list;

	if (!list)
		return (0);

	while (fast_ptr && slow_ptr && fast_ptr->next)
	{
		slow_ptr = slow_ptr->next;
		fast_ptr = fast_ptr->next->next;

		if (fast_ptr == slow_ptr)
			return (1);

	}
	return (0);
}
