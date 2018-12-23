import cv2
import numpy as np
import string

# https://stackoverflow.com/questions/51091865/how-to-extract-these-6-symbols-signatures-from-paper-opencv

rgb_image = cv2.imread('wishlist.png')

#--- Image was too big hence I resized it ---
rgb_image = cv2.resize(rgb_image, (0, 0), fx = 0.25, fy = 0.25)
rgb_height, rgb_width, rgb_channels = rgb_image.shape

#cv2.imshow('image', image)

#--- Converting image to grayscale ---
gray = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2GRAY)

#--- Performing inverted binary threshold ---
retval, thresh_gray = cv2.threshold(gray, 0, 255, type = cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

#--- finding contours ---
image, contours, hierarchy = cv2.findContours(thresh_gray,cv2.RETR_EXTERNAL, \
                                              cv2.CHAIN_APPROX_SIMPLE)
img_height, img_width = image.shape

# cv2.imshow('sign_thresh_gray', thresh_gray)

#--- get all glyphs ---
glyphs = []
for i, c in enumerate(contours):
    # if cv2.contourArea(c) > 100
    x, y, w, h = cv2.boundingRect(c)
    roi = image[y:y+h, x:x+w]

    glyphs.append({
        'rect': cv2.boundingRect(c),
        'img': roi,
    })

    # cv2.imshow(f'i={i},size={w}x{h}', roi)
    # cv2.waitKey()


# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_template_matching/py_template_matching.html
# From here, do detection and compare each glyph

def detect_template(base, template):
    threshold = 0.5
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(base,template,cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)

    points = []
    for pt in zip(*loc[::-1]):
        pt_top_left = pt
        pt_bottom_right = (pt[0] + w, pt[1] + h)
        points.append((pt_top_left, pt_bottom_right))
    return points
        # cv2.rectangle(rgb_image, pt, pt_bottom_right, (0,0,255), 2)

def check_similar(base, template):
    try:
        p = detect_template(base, template)
        if len(p) == 0:
            return False
        return True
    except:
        return False

print('len(glyph)', len(glyphs))

CHARSET = (string.ascii_uppercase+'1234567890')

alphabet_index = 0
for g in glyphs:
    if 'symbol' in g:
        continue

    # if unassigned, place a new alphabet
    # and do so for find similar ones too
    g['symbol'] = CHARSET[alphabet_index]
    alphabet_index += 1
    print('alphabet_index', alphabet_index)

    for f in glyphs:
        if 'symbol' in f:
            continue
        if check_similar(f['img'], g['img']):
            f['symbol'] = g['symbol']

# Now arrange the symbols in rows of y and col of x.
overall_lines = [] # store overall lines
y_lines = [] # store current line, pending. Which is iterated until an entire empty space
y_lines_index = 0
y_lines_next = True

y_center = 0
y_fuzz = 10
y_step = 5
while y_center < img_height:
    y_lower = y_center - y_fuzz
    y_upper = y_center + y_fuzz
    x_symbols = []
    for g in glyphs:
        x, y, w, h = g['rect']
        symbol = g['symbol']
        if y_lower < y and y < y_upper:
            x_symbols.append([x, symbol])
        else:
            continue
    # print(x_symbols)

    x_symbols = sorted(x_symbols, key=lambda kv: kv[0])
    for i, sym in enumerate(x_symbols):
        if (i+1) == len(x_symbols):
            break
        x1, s1 = x_symbols[i]
        x2, s2 = x_symbols[i+1]

        if (x2 - x1) > 35:
            (x_symbols[i])[1] = s1 + ' '

    # join lines together to a sentence
    x_symbols = list(map(lambda kv: kv[1], x_symbols))
    x_symbols = ''.join(x_symbols)
    print(f"{y_center}~{y_fuzz} -> {x_symbols}")
    y_lines.append(x_symbols)

    # do thresholding by choosing longest line in each region
    if y_lines_next == False and len(x_symbols) == 0:
        y_lines_next = True
        # choose longest string in the plot
        longest_str = max(y_lines, key=lambda line: len(line.replace(' ', '')))
        overall_lines.append(longest_str)
        y_lines = []

    if len(x_symbols) != 0:
        y_lines_next = False
    
    y_center += y_step


overall_lines = '\n'.join(overall_lines)
print("Output:")
print(overall_lines)
with open('output.txt', 'w') as out:
    out.write(overall_lines)

# Write it out visually
for g in glyphs:
    x, y, w, h = g['rect']
    symbol = g['symbol']

    font                   = cv2.FONT_HERSHEY_SIMPLEX
    fontScale              = 0.5
    fontColor              = (0,0,255)
    bottomLeftCornerOfText = (x, y-8)
    lineType               = 2
    cv2.putText(rgb_image, symbol, 
        bottomLeftCornerOfText, 
        font, fontScale, fontColor, lineType)

# cv2.imshow('final', rgb_image)
# cv2.waitKey()
cv2.imwrite('output.png', rgb_image)

cv2.destroyAllWindows()

'''
threshold = 0.8
template = glyphs[0]['image']
w, h = template.shape[::-1]
res = cv2.matchTemplate(thresh_gray,template,cv2.TM_CCOEFF_NORMED)
loc = np.where( res >= threshold)

for pt in zip(*loc[::-1]):
    print("pt",pt, f"size={w}x{h}")
    pt_top_left = pt
    pt_bottom_right = (pt[0] + w, pt[1] + h)
    cv2.rectangle(rgb_image, pt, pt_bottom_right, (0,0,255), 2)

cv2.imshow(f'template', template)
cv2.imshow('final', rgb_image)
cv2.waitKey()
'''
