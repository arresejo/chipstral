0x0200	V[0xa] = 0x2
0x0202	V[0xb] = 0xc
0x0204	V[0xc] = 0x3f
0x0206	V[0xd] = 0xc
0x0208	I = 0x2ea
0x020a	draw_sprite(0xa, 0xb, 0x6)
0x020c	draw_sprite(0xc, 0xd, 0x6)
0x020e	V[0xe] = 0x0
0x0210	stack.append(PC); PC = 0x2d4
0x0212	V[0x6] = 0x3
0x0214	V[0x8] = 0x2
0x0216	V[0x0] = 0x60
0x0218	DT = V[0x0]
0x021a	V[0x0] = DT
0x021c	PC += 2 if V[0x0] == 0x0 else 0
0x021e	PC = 0x21a
0x0220	V[0x7] = random.randint(0, 255) & 0x17
0x0222	V[0x7] = (V[0x7] + 0x8) & 0xFF
0x0224	V[0x9] = 0xff
0x0226	I = 0x2f0
0x0228	draw_sprite(0x6, 0x7, 0x1)
0x022a	I = 0x2ea
0x022c	draw_sprite(0xa, 0xb, 0x6)
0x022e	draw_sprite(0xc, 0xd, 0x6)
0x0230	V[0x0] = 0x1
0x0232	PC += 2 if not keys[V[0x0]] else 0
0x0234	V[0xb] = (V[0xb] + 0xfe) & 0xFF
0x0236	V[0x0] = 0x4
0x0238	PC += 2 if not keys[V[0x0]] else 0
0x023a	V[0xb] = (V[0xb] + 0x2) & 0xFF
0x023c	V[0x0] = 0x1f
0x023e	V[0xb] = V[0xb] & V[0x0]
0x0240	draw_sprite(0xa, 0xb, 0x6)
0x0242	V[0xd] = V[0x7]
0x0244	V[0x0] = random.randint(0, 255) & 0xa
0x0246	V[0xd] = (V[0xd] + 0xfe) & 0xFF
0x0248	PC += 2 if V[0x0] != 0x0 else 0
0x024a	V[0xd] = (V[0xd] + 0x2) & 0xFF
0x024c	V[0x0] = 0x0
0x024e	V[0x0] = 0x1f
0x0250	V[0xd] = V[0xd] & V[0x0]
0x0252	draw_sprite(0xc, 0xd, 0x6)
0x0254	I = 0x2f0
0x0256	draw_sprite(0x6, 0x7, 0x1)
0x0258	result = V[0x6] + V[0x8]; V[0x6] = result & 0xFF; V[0xF] = 1 if result > 0xFF else 0; 
0x025a	result = V[0x7] + V[0x9]; V[0x7] = result & 0xFF; V[0xF] = 1 if result > 0xFF else 0; 
0x025c	V[0x0] = 0x3f
0x025e	V[0x6] = V[0x6] & V[0x0]
0x0260	V[0x1] = 0x1f
0x0262	V[0x7] = V[0x7] & V[0x1]
0x0264	PC += 2 if V[0x6] != 0x2 else 0
0x0266	PC = 0x278
0x0268	PC += 2 if V[0x6] != 0x3f else 0
0x026a	PC = 0x282
0x026c	PC += 2 if V[0x7] != 0x1f else 0
0x026e	V[0x9] = 0xff
0x0270	PC += 2 if V[0x7] != 0x00 else 0
0x0272	V[0x9] = 0x1
0x0274	draw_sprite(0x6, 0x7, 0x1)
0x0276	PC = 0x22a
0x0278	V[0x8] = 0x2
0x027a	V[0x3] = 0x1
0x027c	V[0x0] = V[0x7]
0x027e	borrow = 1 if V[0x0] >= V[0xb] else 0; V[0x0] = (V[0x0] - V[0xb]) & 0xFF; V[0xF] = borrow
0x0280	PC = 0x28a
0x0282	V[0x8] = 0xfe
0x0284	V[0x3] = 0xa
0x0286	V[0x0] = V[0x7]
0x0288	borrow = 1 if V[0x0] >= V[0xd] else 0; V[0x0] = (V[0x0] - V[0xd]) & 0xFF; V[0xF] = borrow
0x028a	PC += 2 if V[0xf] == 0x1 else 0
0x028c	PC = 0x2a2
0x028e	V[0x1] = 0x2
0x0290	borrow = 1 if V[0x0] >= V[0x1] else 0; V[0x0] = (V[0x0] - V[0x1]) & 0xFF; V[0xF] = borrow
0x0292	PC += 2 if V[0xf] == 0x1 else 0
0x0294	PC = 0x2ba
0x0296	borrow = 1 if V[0x0] >= V[0x1] else 0; V[0x0] = (V[0x0] - V[0x1]) & 0xFF; V[0xF] = borrow
0x0298	PC += 2 if V[0xf] == 0x1 else 0
0x029a	PC = 0x2c8
0x029c	borrow = 1 if V[0x0] >= V[0x1] else 0; V[0x0] = (V[0x0] - V[0x1]) & 0xFF; V[0xF] = borrow
0x029e	PC += 2 if V[0xf] == 0x1 else 0
0x02a0	PC = 0x2c2
0x02a2	V[0x0] = 0x20
0x02a4	ST = V[0x0]
0x02a6	stack.append(PC); PC = 0x2d4
0x02a8	result = V[0xe] + V[0x3]; V[0xe] = result & 0xFF; V[0xF] = 1 if result > 0xFF else 0; 
0x02aa	stack.append(PC); PC = 0x2d4
0x02ac	V[0x6] = 0x3e
0x02ae	PC += 2 if V[0x3] == 0x1 else 0
0x02b0	V[0x6] = 0x3
0x02b2	V[0x8] = 0xfe
0x02b4	PC += 2 if V[0x3] == 0x1 else 0
0x02b6	V[0x8] = 0x2
0x02b8	PC = 0x216
0x02ba	V[0x9] = (V[0x9] + 0xff) & 0xFF
0x02bc	PC += 2 if V[0x9] != 0xfe else 0
0x02be	V[0x9] = 0xff
0x02c0	PC = 0x2c8
0x02c2	V[0x9] = (V[0x9] + 0x1) & 0xFF
0x02c4	PC += 2 if V[0x9] != 0x2 else 0
0x02c6	V[0x9] = 0x1
0x02c8	V[0x0] = 0x4
0x02ca	ST = V[0x0]
0x02cc	V[0x6] = (V[0x6] + 0x1) & 0xFF
0x02ce	PC += 2 if V[0x6] != 0x40 else 0
0x02d0	V[0x6] = (V[0x6] + 0xfe) & 0xFF
0x02d2	PC = 0x26c
0x02d4	I = 0x2f2
0x02d6	value = V[0xe]; memory[I] = value // 100; memory[I + 1] = (value // 10) % 10; memory[I + 2] = value % 10
0x02d8	V[:0x2 + 1] = memory[I:I + 0x2 + 1]
0x02da	I = (V[0x1] & 0x0F) * 5
0x02dc	V[0x4] = 0x14
0x02de	V[0x5] = 0x0
0x02e0	draw_sprite(0x4, 0x5, 0x5)
0x02e2	V[0x4] = (V[0x4] + 0x15) & 0xFF
0x02e4	I = (V[0x2] & 0x0F) * 5
0x02e6	draw_sprite(0x4, 0x5, 0x5)
0x02e8	PC = stack.pop()
0x02ea	DB 0x80
0x02eb	DB 0x80
0x02ec	DB 0x80
0x02ed	DB 0x80
0x02ee	DB 0x80
0x02ef	DB 0x80
0x02f0	DB 0x80
0x02f1	DB 0x00
0x02f2	DB 0x00
0x02f3	DB 0x00
0x02f4	DB 0x00
0x02f5	DB 0x00
