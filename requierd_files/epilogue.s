

	push {r0, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12}

	pop {r0}
	mov r1, r0
	ldr r0, =string
	bl printf

	pop {r1}
	mov r1, r1
	ldr r0, =string
	bl printf

	pop {r2}
	mov r1, r2
	ldr r0, =string
	bl printf

	pop {r3}
	mov r1, r3
	ldr r0, =string
	bl printf

	pop {r4}
	mov r1, r4
	ldr r0, =string
	bl printf

	pop {r5}
	mov r1, r5
	ldr r0, =string
	bl printf

	pop {r6}
	mov r1, r6
	ldr r0, =string
	bl printf

	pop {r7}
	mov r1, r7
	ldr r0, =string
	bl printf

	pop {r8}
	mov r1, r8
	ldr r0, =string
	bl printf

	pop {r9}
	mov r1, r9
	ldr r0, =string
	bl printf

	pop {r10}
	mov r1, r10
	ldr r0, =string
	bl printf

	pop {r11}
	mov r1, r11
	ldr r0, =string
	bl printf

	pop {r12}
	mov r1, r12
	ldr r0, =string
	bl printf

	ldmfd sp!, {lr}
	bx lr

.data

string: .asciz "%d\n"

