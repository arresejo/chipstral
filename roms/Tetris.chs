0x0200	I = 0x2b4
0x0202	stack.append(PC); PC = 0x3e6
0x0204	stack.append(PC); PC = 0x2b6
0x0206	V[0x0] = (V[0x0] + 0x1) & 0xFF
0x0208	draw_sprite(0x0, 0x1, 0x1)
0x020a	PC += 2 if V[0x0] == 0x25 else 0
0x020c	PC = 0x206
0x020e	V[0x1] = (V[0x1] + 0xff) & 0xFF
0x0210	draw_sprite(0x0, 0x1, 0x1)
0x0212	V[0x0] = 0x1a
0x0214	draw_sprite(0x0, 0x1, 0x1)
0x0216	V[0x0] = 0x25
0x0218	PC += 2 if V[0x1] == 0x00 else 0
0x021a	PC = 0x20e
0x021c	V[0x4] = random.randint(0, 255) & 0x70
0x021e	PC += 2 if V[0x4] != 0x70 else 0
0x0220	PC = 0x21c
0x0222	V[0x3] = random.randint(0, 255) & 0x03
0x0224	V[0x0] = 0x1e
0x0226	V[0x1] = 0x3
0x0228	stack.append(PC); PC = 0x25c
0x022a	DT = V[0x5]
0x022c	draw_sprite(0x0, 0x1, 0x4)
0x022e	PC += 2 if V[0xf] == 0x1 else 0
0x0230	PC = 0x23c
0x0232	draw_sprite(0x0, 0x1, 0x4)
0x0234	V[0x1] = (V[0x1] + 0xff) & 0xFF
0x0236	draw_sprite(0x0, 0x1, 0x4)
0x0238	stack.append(PC); PC = 0x340
0x023a	PC = 0x21c
0x023c	PC += 2 if not keys[V[0x7]] else 0
0x023e	stack.append(PC); PC = 0x272
0x0240	PC += 2 if not keys[V[0x8]] else 0
0x0242	stack.append(PC); PC = 0x284
0x0244	PC += 2 if not keys[V[0x9]] else 0
0x0246	stack.append(PC); PC = 0x296
0x0248	PC += 2 if keys[V[0x2]] else 0
0x024a	PC = 0x250
0x024c	V[0x6] = 0x0
0x024e	DT = V[0x6]
0x0250	V[0x6] = DT
0x0252	PC += 2 if V[0x6] == 0x00 else 0
0x0254	PC = 0x23c
0x0256	draw_sprite(0x0, 0x1, 0x4)
0x0258	V[0x1] = (V[0x1] + 0x1) & 0xFF
0x025a	PC = 0x22a
0x025c	I = 0x2c4
0x025e	I = (I + V[0x4]) & 0xFFFF
0x0260	V[0x6] = 0x0
0x0262	PC += 2 if V[0x3] != 0x1 else 0
0x0264	V[0x6] = 0x4
0x0266	PC += 2 if V[0x3] != 0x2 else 0
0x0268	V[0x6] = 0x8
0x026a	PC += 2 if V[0x3] != 0x3 else 0
0x026c	V[0x6] = 0xc
0x026e	I = (I + V[0x6]) & 0xFFFF
0x0270	PC = stack.pop()
0x0272	draw_sprite(0x0, 0x1, 0x4)
0x0274	V[0x0] = (V[0x0] + 0xff) & 0xFF
0x0276	stack.append(PC); PC = 0x334
0x0278	PC += 2 if V[0xf] == 0x1 else 0
0x027a	PC = stack.pop()
0x027c	draw_sprite(0x0, 0x1, 0x4)
0x027e	V[0x0] = (V[0x0] + 0x1) & 0xFF
0x0280	stack.append(PC); PC = 0x334
0x0282	PC = stack.pop()
0x0284	draw_sprite(0x0, 0x1, 0x4)
0x0286	V[0x0] = (V[0x0] + 0x1) & 0xFF
0x0288	stack.append(PC); PC = 0x334
0x028a	PC += 2 if V[0xf] == 0x1 else 0
0x028c	PC = stack.pop()
0x028e	draw_sprite(0x0, 0x1, 0x4)
0x0290	V[0x0] = (V[0x0] + 0xff) & 0xFF
0x0292	stack.append(PC); PC = 0x334
0x0294	PC = stack.pop()
0x0296	draw_sprite(0x0, 0x1, 0x4)
0x0298	V[0x3] = (V[0x3] + 0x1) & 0xFF
0x029a	PC += 2 if V[0x3] != 0x4 else 0
0x029c	V[0x3] = 0x0
0x029e	stack.append(PC); PC = 0x25c
0x02a0	stack.append(PC); PC = 0x334
0x02a2	PC += 2 if V[0xf] == 0x1 else 0
0x02a4	PC = stack.pop()
0x02a6	draw_sprite(0x0, 0x1, 0x4)
0x02a8	V[0x3] = (V[0x3] + 0xff) & 0xFF
0x02aa	PC += 2 if V[0x3] != 0xff else 0
0x02ac	V[0x3] = 0x3
0x02ae	stack.append(PC); PC = 0x25c
0x02b0	stack.append(PC); PC = 0x334
0x02b2	PC = stack.pop()
0x02b4	DB 0x80
0x02b5	DB 0x00
0x02b6	V[0x7] = 0x5
0x02b8	V[0x8] = 0x6
0x02ba	V[0x9] = 0x4
0x02bc	V[0x1] = 0x1f
0x02be	V[0x5] = 0x10
0x02c0	V[0x2] = 0x7
0x02c2	PC = stack.pop()
0x02c4	DB 0x40
0x02c5	DB 0xe0
0x02c6	DB 0x00
0x02c7	DB 0x00
0x02c8	DB 0x40
0x02c9	DB 0xc0
0x02ca	DB 0x40
0x02cb	DB 0x00
0x02cc	DB 0x00
0x02cd	DB 0xe0
0x02ce	DB 0x40
0x02cf	DB 0x00
0x02d0	DB 0x40
0x02d1	DB 0x60
0x02d2	DB 0x40
0x02d3	DB 0x00
0x02d4	DB 0x40
0x02d5	DB 0x40
0x02d6	DB 0x60
0x02d7	DB 0x00
0x02d8	DB 0x20
0x02d9	DB 0xe0
0x02da	DB 0x00
0x02db	DB 0x00
0x02dc	DB 0xc0
0x02dd	DB 0x40
0x02de	DB 0x40
0x02df	DB 0x00
0x02e0	DB 0x00
0x02e1	DB 0xe0
0x02e2	DB 0x80
0x02e3	DB 0x00
0x02e4	DB 0x40
0x02e5	DB 0x40
0x02e6	DB 0xc0
0x02e7	DB 0x00
0x02e8	DB 0x00
0x02e9	DB 0xe0
0x02ea	DB 0x20
0x02eb	DB 0x00
0x02ec	DB 0x60
0x02ed	DB 0x40
0x02ee	DB 0x40
0x02ef	DB 0x00
0x02f0	DB 0x80
0x02f1	DB 0xe0
0x02f2	DB 0x00
0x02f3	DB 0x00
0x02f4	DB 0x40
0x02f5	DB 0xc0
0x02f6	DB 0x80
0x02f7	DB 0x00
0x02f8	DB 0xc0
0x02f9	DB 0x60
0x02fa	DB 0x00
0x02fb	DB 0x00
0x02fc	DB 0x40
0x02fd	DB 0xc0
0x02fe	DB 0x80
0x02ff	DB 0x00
0x0300	DB 0xc0
0x0301	DB 0x60
0x0302	DB 0x00
0x0303	DB 0x00
0x0304	DB 0x80
0x0305	DB 0xc0
0x0306	DB 0x40
0x0307	DB 0x00
0x0308	DB 0x00
0x0309	DB 0x60
0x030a	DB 0xc0
0x030b	DB 0x00
0x030c	DB 0x80
0x030d	DB 0xc0
0x030e	DB 0x40
0x030f	DB 0x00
0x0310	DB 0x00
0x0311	DB 0x60
0x0312	DB 0xc0
0x0313	DB 0x00
0x0314	DB 0xc0
0x0315	DB 0xc0
0x0316	DB 0x00
0x0317	DB 0x00
0x0318	DB 0xc0
0x0319	DB 0xc0
0x031a	DB 0x00
0x031b	DB 0x00
0x031c	DB 0xc0
0x031d	DB 0xc0
0x031e	DB 0x00
0x031f	DB 0x00
0x0320	DB 0xc0
0x0321	DB 0xc0
0x0322	DB 0x00
0x0323	DB 0x00
0x0324	DB 0x40
0x0325	DB 0x40
0x0326	DB 0x40
0x0327	DB 0x40
0x0328	DB 0x00
0x0329	DB 0xf0
0x032a	DB 0x00
0x032b	DB 0x00
0x032c	DB 0x40
0x032d	DB 0x40
0x032e	DB 0x40
0x032f	DB 0x40
0x0330	DB 0x00
0x0331	DB 0xf0
0x0332	DB 0x00
0x0333	DB 0x00
0x0334	draw_sprite(0x0, 0x1, 0x4)
0x0336	V[0x6] = 0x35
0x0338	V[0x6] = (V[0x6] + 0xff) & 0xFF
0x033a	PC += 2 if V[0x6] == 0x00 else 0
0x033c	PC = 0x338
0x033e	PC = stack.pop()
0x0340	I = 0x2b4
0x0342	V[0xc] = V[0x1]
0x0344	PC += 2 if V[0xc] == 0x1e else 0
0x0346	V[0xc] = (V[0xc] + 0x1) & 0xFF
0x0348	PC += 2 if V[0xc] == 0x1e else 0
0x034a	V[0xc] = (V[0xc] + 0x1) & 0xFF
0x034c	PC += 2 if V[0xc] == 0x1e else 0
0x034e	V[0xc] = (V[0xc] + 0x1) & 0xFF
0x0350	stack.append(PC); PC = 0x35e
0x0352	PC += 2 if V[0xb] != 0xa else 0
0x0354	stack.append(PC); PC = 0x372
0x0356	PC += 2 if V[0x1] != V[0xc] else 0
0x0358	PC = stack.pop()
0x035a	V[0x1] = (V[0x1] + 0x1) & 0xFF
0x035c	PC = 0x350
0x035e	V[0x0] = 0x1b
0x0360	V[0xb] = 0x0
0x0362	draw_sprite(0x0, 0x1, 0x1)
0x0364	PC += 2 if V[0xf] == 0x00 else 0
0x0366	V[0xb] = (V[0xb] + 0x1) & 0xFF
0x0368	draw_sprite(0x0, 0x1, 0x1)
0x036a	V[0x0] = (V[0x0] + 0x1) & 0xFF
0x036c	PC += 2 if V[0x0] == 0x25 else 0
0x036e	PC = 0x362
0x0370	PC = stack.pop()
0x0372	V[0x0] = 0x1b
0x0374	draw_sprite(0x0, 0x1, 0x1)
0x0376	V[0x0] = (V[0x0] + 0x1) & 0xFF
0x0378	PC += 2 if V[0x0] == 0x25 else 0
0x037a	PC = 0x374
0x037c	V[0xe] = V[0x1]
0x037e	V[0xd] = V[0xe]
0x0380	V[0xe] = (V[0xe] + 0xff) & 0xFF
0x0382	V[0x0] = 0x1b
0x0384	V[0xb] = 0x0
0x0386	draw_sprite(0x0, 0xe, 0x1)
0x0388	PC += 2 if V[0xf] == 0x00 else 0
0x038a	PC = 0x390
0x038c	draw_sprite(0x0, 0xe, 0x1)
0x038e	PC = 0x394
0x0390	draw_sprite(0x0, 0xd, 0x1)
0x0392	V[0xb] = (V[0xb] + 0x1) & 0xFF
0x0394	V[0x0] = (V[0x0] + 0x1) & 0xFF
0x0396	PC += 2 if V[0x0] == 0x25 else 0
0x0398	PC = 0x386
0x039a	PC += 2 if V[0xb] != 0x00 else 0
0x039c	PC = 0x3a6
0x039e	V[0xd] = (V[0xd] + 0xff) & 0xFF
0x03a0	V[0xe] = (V[0xe] + 0xff) & 0xFF
0x03a2	PC += 2 if V[0xd] == 0x1 else 0
0x03a4	PC = 0x382
0x03a6	stack.append(PC); PC = 0x3c0
0x03a8	PC += 2 if V[0xf] == 0x1 else 0
0x03aa	stack.append(PC); PC = 0x3c0
0x03ac	V[0xa] = (V[0xa] + 0x1) & 0xFF
0x03ae	stack.append(PC); PC = 0x3c0
0x03b0	V[0x0] = V[0xa]
0x03b2	V[0xd] = 0x7
0x03b4	V[0x0] = V[0x0] & V[0xd]
0x03b6	PC += 2 if V[0x0] != 0x4 else 0
0x03b8	V[0x5] = (V[0x5] + 0xfe) & 0xFF
0x03ba	PC += 2 if V[0x5] != 0x2 else 0
0x03bc	V[0x5] = 0x4
0x03be	PC = stack.pop()
0x03c0	I = 0x700
0x03c2	memory[I:I + 0x2 + 1] = V[:0x2 + 1]
0x03c4	I = 0x804
0x03c6	value = V[0xa]; memory[I] = value // 100; memory[I + 1] = (value // 10) % 10; memory[I + 2] = value % 10
0x03c8	V[:0x2 + 1] = memory[I:I + 0x2 + 1]
0x03ca	I = (V[0x0] & 0x0F) * 5
0x03cc	V[0xd] = 0x32
0x03ce	V[0xe] = 0x0
0x03d0	draw_sprite(0xd, 0xe, 0x5)
0x03d2	V[0xd] = (V[0xd] + 0x5) & 0xFF
0x03d4	I = (V[0x1] & 0x0F) * 5
0x03d6	draw_sprite(0xd, 0xe, 0x5)
0x03d8	V[0xd] = (V[0xd] + 0x5) & 0xFF
0x03da	I = (V[0x2] & 0x0F) * 5
0x03dc	draw_sprite(0xd, 0xe, 0x5)
0x03de	I = 0x700
0x03e0	V[:0x2 + 1] = memory[I:I + 0x2 + 1]
0x03e2	I = 0x2b4
0x03e4	PC = stack.pop()
0x03e6	V[0xa] = 0x0
0x03e8	V[0x0] = 0x19
0x03ea	PC = stack.pop()
0x03ec	DB 0x37
0x03ed	DB 0x23