import whisper
import os
import tempfile
import pyaudio
import wave
import numpy as np
from typing import Optional, Dict, Any

class gmtSpeechReco:
    """
    Speech recognition class using Whisper
    Supports Hindi, English, and other languages
    """
    
    def __init__(self, model_size: str = "base"):
        """
        Initialize the speech recognition model
        
        Args:
            model_size: Whisper model size (tiny, base, small, medium, large)
        """
        self.model = whisper.load_model(model_size)
        self.supported_languages = {
            'en': 'English',
            'hi': 'Hindi', 
            'es': 'Spanish',
            'fr': 'French',
            'de': 'German',
            'it': 'Italian',
            'pt': 'Portuguese',
            'ru': 'Russian',
            'ja': 'Japanese',
            'ko': 'Korean',
            'zh': 'Chinese',
            'ar': 'Arabic',
            'bn': 'Bengali',
            'ta': 'Tamil',
            'te': 'Telugu',
            'mr': 'Marathi',
            'gu': 'Gujarati',
            'kn': 'Kannada',
            'ml': 'Malayalam',
            'pa': 'Punjabi',
            'ur': 'Urdu'
        }
    
    def transcribe_audio(self, audio_file_path: str, language: Optional[str] = None) -> Dict[str, Any]:
        """
        Transcribe audio file to text
        
        Args:
            audio_file_path: Path to the audio file
            language: Language code (optional, auto-detect if not provided)
            
        Returns:
            Dictionary containing transcription results
        """
        try:
            # Transcribe the audio
            if language and language in self.supported_languages:
                result = self.model.transcribe(audio_file_path, language=language)
            else:
                result = self.model.transcribe(audio_file_path)
            
            return {
                'success': True,
                'text': result['text'].strip(),
                'language': result.get('language', 'unknown'),
                'segments': result.get('segments', []),
                'error': None
            }
            
        except Exception as e:
            return {
                'success': False,
                'text': '',
                'language': None,
                'segments': [],
                'error': str(e)
            }
    
    def transcribe_audio_data(self, audio_data: bytes, language: Optional[str] = None) -> Dict[str, Any]:
        """
        Transcribe audio data (bytes) to text
        
        Args:
            audio_data: Raw audio data in bytes
            language: Language code (optional, auto-detect if not provided)
            
        Returns:
            Dictionary containing transcription results
        """
        # Create temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as temp_file:
            temp_file.write(audio_data)
            temp_file_path = temp_file.name
        
        try:
            # Transcribe the temporary file
            result = self.transcribe_audio(temp_file_path, language)
            return result
            
        finally:
            # Clean up temporary file
            if os.path.exists(temp_file_path):
                os.unlink(temp_file_path)
    
    def get_supported_languages(self) -> Dict[str, str]:
        """
        Get list of supported languages
        
        Returns:
            Dictionary mapping language codes to language names
        """
        return self.supported_languages.copy()
    
    def record_audio(self, duration: int = 5, sample_rate: int = 16000, channels: int = 1) -> str:
        """
        Record audio from microphone for specified duration
        
        Args:
            duration: Recording duration in seconds
            sample_rate: Audio sample rate
            channels: Number of audio channels
            
        Returns:
            Path to the recorded audio file
        """
        print(f"Recording audio for {duration} seconds...")
        print("Speak now!")
        
        # Audio parameters
        chunk = 1024
        format = pyaudio.paInt16
        
        # Initialize PyAudio
        p = pyaudio.PyAudio()
        
        # Open stream
        stream = p.open(format=format,
                       channels=channels,
                       rate=sample_rate,
                       input=True,
                       frames_per_buffer=chunk)
        
        frames = []
        
        # Record for specified duration
        for i in range(0, int(sample_rate / chunk * duration)):
            data = stream.read(chunk, exception_on_overflow=False)
            frames.append(data)
            
            # Progress indicator
            if i % (sample_rate // chunk) == 0:
                seconds_elapsed = i * chunk // sample_rate
                print(f"Recording: {seconds_elapsed}s/{duration}s", end='\r')
        
        print("\nRecording finished!")
        
        # Stop and close the stream
        stream.stop_stream()
        stream.close()
        p.terminate()
        
        # Save to temporary file
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.wav')
        temp_file_path = temp_file.name
        temp_file.close()
        
        # Write audio data to file
        wf = wave.open(temp_file_path, 'wb')
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(format))
        wf.setframerate(sample_rate)
        wf.writeframes(b''.join(frames))
        wf.close()
        
        return temp_file_path
    
    def record_and_transcribe(self, duration: int = 5, language: Optional[str] = None) -> Dict[str, Any]:
        """
        Record audio and transcribe it immediately
        
        Args:
            duration: Recording duration in seconds
            language: Language code (optional, auto-detect if not provided)
            
        Returns:
            Dictionary containing transcription results
        """
        try:
            # Record audio
            audio_file = self.record_audio(duration)
            
            # Transcribe the recorded audio
            result = self.transcribe_audio(audio_file, language)
            
            # Clean up the temporary file
            if os.path.exists(audio_file):
                os.unlink(audio_file)
            
            return result
            
        except Exception as e:
            return {
                'success': False,
                'text': '',
                'language': None,
                'segments': [],
                'error': str(e)
            }
    
    def start_realtime_recognition(self, chunk_duration: int = 3, language: Optional[str] = None):
        """
        Start real-time speech recognition
        Records and transcribes audio in chunks
        
        Args:
            chunk_duration: Duration of each audio chunk in seconds
            language: Language code (optional, auto-detect if not provided)
        """
        print("Starting real-time speech recognition...")
        print("Press Ctrl+C to stop")
        
        try:
            while True:
                # Record a chunk of audio
                print(f"\nRecording {chunk_duration} second chunk...")
                result = self.record_and_transcribe(chunk_duration, language)
                
                if result['success'] and result['text'].strip():
                    print(f"Transcription: {result['text']}")
                    print(f"Language: {self.supported_languages.get(result['language'], result['language'])}")
                elif result['error']:
                    print(f"Error: {result['error']}")
                
        except KeyboardInterrupt:
            print("\nReal-time recognition stopped.")
    
    def detect_language(self, audio_file_path: str) -> str:
        """
        Detect the language of the audio
        
        Args:
            audio_file_path: Path to the audio file
            
        Returns:
            Language code
        """
        try:
            # Load audio and pad/trim it to fit 30 seconds
            audio = whisper.load_audio(audio_file_path)
            audio = whisper.pad_or_trim(audio)
            
            # Make log-Mel spectrogram and move to the same device as the model
            mel = whisper.log_mel_spectrogram(audio).to(self.model.device)
            
            # Detect the spoken language
            _, probs = self.model.detect_language(mel)
            detected_lang = max(probs, key=probs.get)
            
            return detected_lang
            
        except Exception as e:
            return 'unknown'

# Example usage and testing
if __name__ == "__main__":
    # Initialize the speech recognition
    speech_recognizer = gmtSpeechReco(model_size="base")
    
    print("=== Speech Recognition Ready ===")
    print("Choose an option:")
    print("1. Record and transcribe (single recording)")
    print("2. Real-time continuous recognition")
    print("3. List supported languages")
    print("4. Test with existing audio file")
    print("5. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == "1":
            # Single recording
            duration = input("Recording duration in seconds (default 5): ").strip()
            duration = int(duration) if duration.isdigit() else 5
            
            lang_choice = input("Language? (en/hi/auto-detect, default auto): ").strip()
            language = lang_choice if lang_choice in ['en', 'hi'] else None
            
            print(f"\nRecording for {duration} seconds...")
            result = speech_recognizer.record_and_transcribe(duration, language)
            
            if result['success']:
                print(f"✓ Transcription: {result['text']}")
                print(f"✓ Language: {speech_recognizer.supported_languages.get(result['language'], result['language'])}")
            else:
                print(f"✗ Error: {result['error']}")
                
        elif choice == "2":
            # Real-time recognition
            chunk_duration = input("Chunk duration in seconds (default 3): ").strip()
            chunk_duration = int(chunk_duration) if chunk_duration.isdigit() else 3
            
            lang_choice = input("Language? (en/hi/auto-detect, default auto): ").strip()
            language = lang_choice if lang_choice in ['en', 'hi'] else None
            
            speech_recognizer.start_realtime_recognition(chunk_duration, language)
            
        elif choice == "3":
            # List languages
            print("\nSupported languages:")
            for code, name in speech_recognizer.get_supported_languages().items():
                print(f"  {code}: {name}")
                
        elif choice == "4":
            # Test with existing file
            file_path = input("Enter audio file path: ").strip()
            if os.path.exists(file_path):
                lang_choice = input("Language? (en/hi/auto-detect, default auto): ").strip()
                language = lang_choice if lang_choice in ['en', 'hi'] else None
                
                result = speech_recognizer.transcribe_audio(file_path, language)
                if result['success']:
                    print(f"✓ Transcription: {result['text']}")
                    print(f"✓ Language: {speech_recognizer.supported_languages.get(result['language'], result['language'])}")
                else:
                    print(f"✗ Error: {result['error']}")
            else:
                print("File not found!")
                
        elif choice == "5":
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")
