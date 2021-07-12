#include <stdio.h>
#include <fcntl.h>

int main(void)
{
	// buffers
  char buffer[0x200];
  char flag[0x200];

  setbuf(stdout, NULL);
  setbuf(stdin, NULL);
  setbuf(stderr, NULL);

	// initializeer geheugen met 0x00 bytes
  memset(buffer, 0, sizeof(buffer));
  memset(flag, 0, sizeof(flag));

	// open flag.txt
  int fd = open("flag.txt", O_RDONLY);
  if (fd == -1) {
    puts("failed to read flag. please contact an admin if this is remote");
    exit(1);
  }

	// lees 512 bytes van flag.txt naar char[] flag
  read(fd, flag, sizeof(flag));
  close(fd);

  puts("what do you say?");

	// lees 512 bytes (511 + 0x00) van stdin
  read(0, buffer, sizeof(buffer) - 1);
	// lees tot aan newline "\n" / 0x0a
  buffer[strcspn(buffer, "\n")] = 0;

	// werk alleen als de buffer met "please" begint
  if (!strncmp(buffer, "please", 6)) {
    printf(buffer); // waarschijnlijk een printf / format string exploit
    puts(" to you too!");
  }
}
