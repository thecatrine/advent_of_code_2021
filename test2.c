    w = *num;num++;
    x = z % 26 + 13;
    z /= 1;

    if (x != w) {
        z = z*26 + w + 15;
    }

    w = *num;num++;
    x = z % 26 + 13;
    z /= 1;

    if (x != w) {
        z = z*26 + w + 16;
    }

    w = *num;num++;
    x = z % 26 + 10;
    z /= 1;

    if (x != w) {
        z = z*26 + w + 4;
    }

    w = *num;num++;
    x = z % 26 + 15;
    z /= 1;

    if (x != w) {
        z = z * 26 + w + 14;
    }


    w = *num;num++;
    x = z % 26 - 8;

    if (x != w) {
        z = z * 26 + w + 1; 
    }

    w = *num;num++;
    x = z % 26 - 10;
    z /= 26;

    if (x != w) {
        z = z * 26 + w + 5;
    }

    w = *num;num++;
    x = z % 26 + 11;
    z /= 1;

    if (x != w) {
        z = z * 26 + w + 1;
    }

    w = *num;num++;
    x = z % 26 - 3;
    z /= 26;

    if (x != w) {
        z = z * 26 + w + 3;
    }

    w = *num;num++;
    x = z % 26 + 14;
    z /= 1;

    if (x != w) {
        z = z * 26 + w + 3;
    }
    w = *num;num++;
    x = z % 26 - 4;
    z /= 26;

    if (x != w) {
        z = z * 26 + w + 7;
    }
    w = *num;num++;
    x = z % 26 + 14;
    z /= 1;

    if (x != w) {
        z = z * 26 + w + 5;
    }
    w = *num;num++;
    x = z % 26 - 5;

    if (x != w) {
        z = z * 26 + w + 13;
    }
    w = *num;num++;
    x = z % 26 - 8;
    z /= 26;

    if (x != w) {
        z = z * 26 + w + 3;
    }
    w = *num;num++;
    x = z % 26 - 11;
    z /= 26;

    if (x != w) { // Can't happen
        z = z * 26 + w + 10; // Can't for z = 0
    }

    if (z == 0) {return 1;} else {return 0;}
}