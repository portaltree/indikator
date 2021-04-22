from time import sleep

cnt = 0


def bar(total, count, cnt, title="Downloading", done_text="#", togo_text=" "):
    ascii_list = ["/", "/", "-", "-", "\\", "\\", "|", "|", "/", "/", "-", "-", "\\", "\\", "|", "|"]

    done = round(round((count + 1) / total * 100, 1) / 10)
    togo = 10 - done

    done_bar = done_text * 2 * int(done)
    togo_bar = togo_text * 2 * int(togo)
    # print(f"{ascii[cnt]} {done} {togo} : {done_bar} {togo_bar}", end="\r")
    print(f"{ascii_list[cnt]} {title}: [{done_bar}{togo_bar}] {count + 1}/{total}", end="\r")
    if count + 1 == total:
        print(f"✓ {title}: [{done_bar}{togo_bar}] {count + 1}/{total}", end="\r")
    sleep(0.1)
