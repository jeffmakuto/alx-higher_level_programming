#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to pointer of first node of listint_t list
 * @num: integer to be inserted
 * Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int num)
{
	listint_t *new_node, *current;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->n = num;
	new_node->next = NULL;

	if (!*head || (*head)->n >= num)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	current = *head;
	while (current->next != NULL && current->next->n < num)
		current = current->next;
	new_node->next = current->next;
	current->next = new_node;

	return (new_node);
}

