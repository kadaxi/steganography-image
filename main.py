from PIL import Image;
import numpy as np;

# -- General
text_default="testing!";
delimiter = "*";

# -- Main
def encode_text(text):
    bin_data = str();
    for c in text:
        bin_data += "".join((bin(ord(c)))).replace("0b","").zfill(8);
    return bin_data;

def decode_text(res_bin):
    res_txt = int(res_bin,2);
    return res_txt.to_bytes((res_txt.bit_length() + 7) // 8, 'big').decode(encoding="utf-8",errors="surrogatepass");

def dec2bin(dec):
    return str(bin(dec)).replace("0b","").zfill(8);

def bin2dec(bin):
    return int(bin,2);

def dec2arrbin(arr_dec):
    return [dec2bin(i) for i in arr_dec];

def swap_pos(col, bit):
    col = dec2bin(col);
    col_mod = (col[:-1] + str(bit));
    return bin2dec(col_mod);

def encode_image(src, txt):
    img = Image.open("images/img1.jpg");
    bitmap = img.load();
    img_wid, img_hei = img.size;
    len_txt = len(txt);
    idx = 0;

    for i in range(img_wid):
        for j in range(img_hei):
            if idx < len_txt:
                r,g,b = img.getpixel((i,j));
                if idx < len_txt:
                    pix_r = swap_pos(r, txt[idx]);
                    idx+=1;
                else:
                    pix_r = r;
                if idx < len_txt:
                    pix_g = swap_pos(g, txt[idx]);
                    idx+=1;
                else:
                    pix_g = g;
                if idx < len_txt:
                    pix_b = swap_pos(b, txt[idx]);
                    idx+=1;
                else:
                    pix_b = b;
                bitmap[i,j] = (pix_r, pix_g, pix_b);
            else:
                break;
        else:
            continue;
        break;
    img.save("out.png");

def decode_image(src):
    img = Image.open("out.png");
    bitmap = img.load();
    byte = "";
    msg = "";

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r,g,b = dec2arrbin(bitmap[i,j]);

            byte += r[-1];
            if len(byte) >= 8:
                if byte == encode_text(delimiter):
                    break;
                msg += byte;
                byte = "";

            byte += g[-1];
            if len(byte) >= 8:
                if byte == encode_text(delimiter):
                    break;
                msg += byte;
                byte = "";

            byte += b[-1];
            if len(byte) >= 8:
                if byte == encode_text(delimiter):
                    break;
                msg += byte;
                byte = "";
        else:
            continue;
        break
    return msg;

def main()->None:
    enc_msg = encode_text((text_default + delimiter));
    enc_img = encode_image("cat.jpg",enc_msg);
    msg = decode_image("out.jpg");
    print("BINARY MESSAGE:",enc_msg[:-8]);
    print("DECODED MESSAGE:", decode_text(msg));

if __name__ == "__main__":
    main();