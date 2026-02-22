import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://lh3.googleusercontent.com/fife/ALs6j_G93rQ5GfD3gE9Uxb_7688N5M_Lw6Lh2d6yWv_qM9y4vU2T1-xRyfH6Hh3QjA9A0TqGq7h0Q8k8N0O0_Yd0A1Y8R8oQ-_7Q1s1H5l9gQ1S0K9V7M2n0_N3R5G8UqY7E0p0Qn5W1S0u6K0Q_90_K5r1Q2x_61K7Y7J3P2S2G9h2m6Y6L1x9H3t0M1Q5W5k9A7o6A2v2q3J3L4l0J0X4d4g4Q6b3v1z5k3d7b8R4G1Q8E1F8e2o5Y7W8Q0W2K0T0g6G3s7g5L4S6Q_5vF4D2z8G8y2s8U1M0Q8W9J7c6a9E4x1D5V0a2I3e6T5E1q2v6Q1d_Q7x9B4E0V0f7T0R9v6L9x0F_5Y0U0y9g9_3U2s2K3J7X8O_7N5j6i3e9M7W1J7J4M9a6v7U5s2w5J0k2J1t1W5k1T5D7A9E1s6x4F41V1y2l1M6k5K1N3e9P6I0o5O2a6I5g2x0V5o2d3C1r5r9N3Z0c4y7J5L1Z1o0X4z0d8y9N1C5H8N9E0G7j6V7Q2M6A2G0K1Q0P4p4M2R9W7g1H0M0O2D5n8Q8B4H4M3a8W2A7c8X3y9B0g6X2R2Q0D0_z7a0A2P5s7V5b7i5j2_8e7E0f8w6q5a6s0S6V1N7L1F8_7g1J8P9K8u9s3d0T4U0i8V5M8i3A3n0J1U4T7b8p0N2T3r4_j3e0W9O2i6M0a1N_v2_9M2s0u5n2d6v8w8A3L4l0I3X7d6W3d8z_5E2H011A8q4C7G1X8k4a6Q2X4x0R9k3f1P_y5j0M6Z4I6q8b_5m4D9_0l6W1K3x7U9E8R4z1A8b6Q1c5p2Y9g0D2I7u7b8k2G4A2k8K5a8f5z6o2A1m6M7p7N5v2U2q3h4N5l7x7M6v6E0c6E9l2v2S0P2Y9E1_3y2T9B7o6m2_4X8D2b1A6j_o5_5v4E1y5P8o1C0D0O_5y2I8L1j5O4a8I9b1G1D9i8I6H6a8_8E7l0g6n5S6C6b61N9A7E1j7P7Y3k5W1U8Q4q6N7D1l3J7J4i2x_7x3T8J6b6T2z0h2J8Q0p5u4E8q7c0S6b9a8w0Z9R4_1B4l3X6x9e3_0U5g9H3w9t6Q2O9A1u7t4r6F8p6d7y6B2d0m8s1x4u9G5y1q9P6_2g8n8y8S_1h0V5E2S7W3U4i6U0M7J2O9W5n2e4y2u1L1O3b6p4_s5w2s0G6C1P4O4C9u8s9y1E3n7W5b6F6n5n7Z5J2Q9E8C7D4m2s9X6H9G4Q2P4D1w1k6i5P0a3R7H7g6D4w7J1_6p3Y5i3Y4H7l3a3=w1000-h1000-no"

req = urllib.request.Request(
    url, 
    data=None, 
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
)

try:
    with urllib.request.urlopen(req) as response, open(r"C:\Users\TestSolutions\Documents\La-Jiraffa\images\onSite\getQuotation\planning_new.jpg", 'wb') as out_file:
        out_file.write(response.read())
    print("Downloaded image.")
    from PIL import Image
    img = Image.open(r"C:\Users\TestSolutions\Documents\La-Jiraffa\images\onSite\getQuotation\planning_new.jpg")
    img.save(r"C:\Users\TestSolutions\Documents\La-Jiraffa\images\onSite\getQuotation\planning_new.webp", 'WEBP', quality=85)
    print("Converted to webp.")
except Exception as e:
    print(f"Error: {e}")
