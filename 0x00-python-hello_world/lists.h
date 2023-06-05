#ifndef LIST_H
#define LIST_H

#include <stdio.h>
#include <stdlib.h>

/* Definition of a singly linked list node */
typedef struct listint_s {
    int data;
    struct listint_s *next;
} listint_t;

/* Prototype */
int check_cycle(listint_t *list);
