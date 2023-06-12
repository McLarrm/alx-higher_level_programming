#ifndef LISTS_H
#define LIST_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* Definition of a singly linked list node */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

/* Prototype */
size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);
int is_palindrome(listint_t **head);

#endif /* LISTS_H */
