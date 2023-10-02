#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle in it.
 * @list: linked list to be checked
 *
 * Return: 1 if the list has a cycle, otherwise 0
 */
int check_cycle(listint_t *list)
{
	listint_t *slow_ptr = list;
	listint_t *fast_ptr = list;

	if (!list)
		return (0);

	while (slow_ptr && fast_ptr && fast_ptr->next)
	{
		slow_ptr = slow_ptr->next;
		fast_ptr = fast_ptr->next->next;
		if (slow_ptr == fast_ptr)
			return (1);
	}

	return (0);
}
