import cv2
import concurrent.futures
import time

# --- Tugas 1: Pemrosesan Gambar (Intensif CPU) ---
def apply_grayscale(frame):
    # Mensimulasikan konversi frame ke skala abu-abu (grayscale)
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# --- Tugas 2: Analisis Fitur (Simulasi) ---
def analyze_brightness(frame):
    # Menghitung rata-rata di seluruh baris, kemudian kolom
    avg_per_channel = frame.mean(axis=0).mean(axis=0) 
    
    # avg_per_channel berisi [B, G, R]. Kita ambil rata-rata dari 3 
    # nilai tersebut untuk mendapatkan satu nilai kecerahan keseluruhan.
    overall_avg = avg_per_channel.mean() 
    
    return f"Avg Brightness: {int(overall_avg)}"

def process_video(video_path):
    cap = cv2.VideoCapture(video_path)
    
    # Kita menggunakan ThreadPoolExecutor untuk I/O dan pemrosesan ringan.
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Task Parallelism: Mengirim dua tugas berbeda untuk frame yang sama
            future_gray = executor.submit(apply_grayscale, frame)
            future_analysis = executor.submit(analyze_brightness, frame)

            # Mengambil hasil (ini menunggu tugas paralel selesai untuk frame INI)
            gray_frame = future_gray.result()
            analysis_text = future_analysis.result()

            # Menampilkan video yang telah diproses
            cv2.putText(gray_frame, analysis_text, (10, 30), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            
            cv2.imshow('Task Parallelism Video Feed', gray_frame)

            # Tekan 'q' untuk keluar
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    process_video("input_video.mp4")