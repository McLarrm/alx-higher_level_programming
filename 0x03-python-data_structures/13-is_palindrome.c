#include "lists.h"

/**
 * reverse_list - reverses a linked list
 * @head: pointer to pointer of the head of the list
 */
void reverse_list(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of the head of the list
 * Return: 0 if not a palindrome, 1 if a palindrome
 */
int is_palindrome(listint_t **head)
{
	int is_palindrome = 1;

	listint_t *slow_ptr = *head;
	listint_t *fast_ptr = *head;
	listint_t *second_half = *head;
	listint_t *prev_slow_ptr = *head;
	listint_t *mid_node = NULL;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast_ptr != NULL && fast_ptr->next != NULL)
		{
			fast_ptr = fast_ptr->next->next;
			prev_slow_ptr = slow_ptr;
			slow_ptr = slow_ptr->next;
		}

		if (fast_ptr != NULL)
		{
			mid_node = slow_ptr;
			slow_ptr = slow_ptr->next;
		}

		second_half = slow_ptr;
		prev_slow_ptr->next = NULL;
		reverse_list(&second_half);

		while (*head != NULL && second_half != NULL)
		{
			if ((*head)->n != second_half->n)
			{
				is_palindrome = 0;
				break;
			}

			*head = (*head)->next;
			second_half = second_half->next;
		}

		reverse_list(&second_half);

		if (mid_node != NULL)
		{
			prev_slow_ptr->next = mid_node;
			mid_node->next = second_half;
		}
		else
		{
			prev_slow_ptr->next = second_half;
		}
	}

	return (is_palindrome);
}
