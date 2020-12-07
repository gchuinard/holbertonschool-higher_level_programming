#include "lists.h"


/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 *
 * @list: the list to verify.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */

int	check_cycle(listint_t *list)
{
	listint_t	*first_node;
	listint_t	*tmp_node;

	first_node = list;
	tmp_node = list->next;
	while (tmp_node != NULL)
	{
		if (tmp_node == first_node)
		{
			return (1);
		}
		tmp_node = tmp_node->next;
	}
	return (0);
}
