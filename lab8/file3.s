	.arch armv8-a
	.file	"file3.c"
	.text
	.align	2
	.global	main
	.type	main, %function
main:
.LFB0:
	.cfi_startproc
	sub	sp, sp, #16
	.cfi_def_cfa_offset 16
	mov	w0, 15
	str	w0, [sp, 12]
	ldr	w0, [sp, 12]
	lsl	w0, w0, 1
	str	w0, [sp, 8]
	ldr	w1, [sp, 12]
	mov	w0, w1
	lsl	w0, w0, 1
	add	w0, w0, w1
	str	w0, [sp, 8]
	mov	w0, 0
	add	sp, sp, 16
	.cfi_def_cfa_offset 0
	ret
	.cfi_endproc
.LFE0:
	.size	main, .-main
	.ident	"GCC: (Debian 10.2.1-6) 10.2.1 20210110"
	.section	.note.GNU-stack,"",@progbits
