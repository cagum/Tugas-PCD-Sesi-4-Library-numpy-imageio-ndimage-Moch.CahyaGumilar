import imageio
import numpy as np
from scipy.ndimage import gaussian_filter, sobel
import matplotlib.pyplot as plt

def process_image(image_path):

    image = imageio.imread(image_path, pilmode='L')
    blurred_image = gaussian_filter(image, sigma=2)

    sobel_x = sobel(blurred_image, axis=0)
    sobel_y = sobel(blurred_image, axis=1)
    edges = np.hypot(sobel_x, sobel_y)

    edges = (edges / np.max(edges) * 255).astype(np.uint8)

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 3, 1)
    plt.imshow(image, cmap='gray')
    plt.title("Original Image")
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(blurred_image, cmap='gray')
    plt.title("Blurred Image (Gaussian)")
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(edges, cmap='gray')
    plt.title("Edges (Sobel)")
    plt.axis('off')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    image_path = "D:\Perkuliahan\S5\Pengolahan Citra Digital\s4\praktikum tugas 4\capmar.jpg"
    process_image(image_path)
