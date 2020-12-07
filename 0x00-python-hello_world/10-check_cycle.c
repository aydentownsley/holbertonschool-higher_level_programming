#include "lists.h"
#include <stdio.h>

int check_cycle(listint_t *list)
{
	while(list->next)
	{
		printf("add of list [%p]\n", list);
		if (list == list->next->next)
			return (1);
		else
			list = list->next;
	}
	return (0);
}
