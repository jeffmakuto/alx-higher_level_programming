#include "lists.h"

/**
 * check_cycle - checks if linked list contains a cycle
 * @list: the list to be checked
 * Return: 1 if cycle is present else 0
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (!list || !list->next)
		return (0);

	slow = list;
	fast = list->next;

	while (fast && fast->next)
	{
		if (slow == fast)
			return (1);

		slow = slow->next;
		fast = fast->next->next;
	}

	return (0);
}
