#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle.
 * @list: Pointer to the head of the linked list.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL || list->next == NULL)
		return (0);

	slow = list;
	fast = list->next;

	while (fast != NULL && fast->next != NULL)
	{
		if (slow == fast)
			return (1);

		slow = slow->next;
		fast = fast->next->next;
	}

	return (0);
}

/**
 * main - Entry point
 *
 * Return: Always 0 (Success)
 */
int main(void)
{
	int hasCycle;

	/* Create a linked list with a cycle */
	listint_t *list = malloc(sizeof(listint_t));
	list->data = 1;
	list->next = malloc(sizeof(listint_t));
	list->next->data = 2;
	list->next->next = malloc(sizeof(listint_t));
	list->next->next->data = 3;
	list->next->next->next = list;

	/* Check if the linked list has a cycle */
	hasCycle = check_cycle(list);
	printf("Has Cycle: %d\n", hasCycle);

	/* Free the allocated memory */
	free(list->next->next);
	free(list->next);
	free(list);

	return (0);
}
