# 🎤 Maiya

**🚧 PARKING PROJECT - Currently Under Development 🚧**

A Python-based speech recognition system using OpenAI Whisper that supports multiple languages including Hindi, English, and 20+ other languages.

**🎯 Part of the Larger Maiya AI System Architecture** - This speech recognition module is a component of the comprehensive Maiya AI ecosystem shown in the system architecture diagram.

## 🌟 Features

- **Multi-language Support**: Hindi, English, Spanish, French, German, and many more
- **Real-time Speech Recognition**: Record and transcribe audio in real-time
- **Language Detection**: Automatically detect the spoken language
- **Flexible Input**: Support for both audio files and microphone recording
- **Interactive Interface**: Easy-to-use command-line menu
- **High Accuracy**: Powered by OpenAI Whisper's state-of-the-art speech recognition

## 🚀 Quick Start

### Prerequisites
```bash
pip install openai-whisper pyaudio numpy
```

### Run the Speech Recognition
```bash
python speechrecogniation.py
```

### Usage Options
1. **Single Recording**: Record and transcribe a single audio clip
2. **Real-time Recognition**: Continuous recording and transcription
3. **Language Support**: View all supported languages
4. **File Processing**: Transcribe existing audio files

## 🎯 Supported Languages

| Language Code | Language Name |
|---------------|---------------|
| en | English |
| hi | Hindi |
| es | Spanish |
| fr | French |
| de | German |
| it | Italian |
| pt | Portuguese |
| ru | Russian |
| ja | Japanese |
| ko | Korean |
| zh | Chinese |
| ar | Arabic |
| bn | Bengali |
| ta | Tamil |
| te | Telugu |
| mr | Marathi |
| gu | Gujarati |
| kn | Kannada |
| ml | Malayalam |
| pa | Punjabi |
| ur | Urdu |

## 💻 Code Example

```python
from speechrecogniation import gmtSpeechReco

# Initialize the speech recognizer
speech_recognizer = gmtSpeechReco(model_size="base")

# Record and transcribe audio
result = speech_recognizer.record_and_transcribe(duration=5, language="hi")

if result['success']:
    print(f"Transcription: {result['text']}")
    print(f"Language: {result['language']}")
else:
    print(f"Error: {result['error']}")
```

## 🔧 Available Methods

### Core Methods
- `record_and_transcribe(duration, language)` - Record and transcribe audio
- `transcribe_audio(file_path, language)` - Transcribe existing audio file
- `start_realtime_recognition(chunk_duration, language)` - Real-time recognition
- `get_supported_languages()` - Get list of supported languages
- `detect_language(audio_file_path)` - Detect language of audio file

### Audio Recording
- `record_audio(duration, sample_rate, channels)` - Record audio from microphone
- `transcribe_audio_data(audio_data, language)` - Transcribe raw audio data

## 🎛️ Model Sizes

Choose different Whisper model sizes based on your needs:

- **tiny**: Fastest, lowest accuracy
- **base**: Good balance of speed and accuracy
- **small**: Better accuracy, slower
- **medium**: High accuracy, much slower
- **large**: Best accuracy, slowest

```python
# Use different model sizes
speech_recognizer = gmtSpeechReco(model_size="small")  # More accurate
```

## 🚧 Current Development Status

This is a **parking project** currently under active development. Features being worked on:

### 🎯 Maiya AI System Integration (From Architecture)
Based on the [Maiya AI System Architecture](index.html), this speech recognition module integrates with:

- [x] **Microphone Capture** ✅ (Implemented)
- [x] **Noise Reduction + Audio Cleanup** ✅ (Basic implementation)
- [x] **Voice Activity Detection (VAD)** ✅ (Basic implementation)
- [x] **Segment Audio Chunks** ✅ (Implemented)
- [x] **Whisper STT Engine** ✅ (Core functionality)
- [x] **Text Normalization & Cleanup** ✅ (Basic implementation)

### 🔄 Next Development Phase
- [ ] **Intent + Emotion Inference** (Natural Language Understanding)
- [ ] **Maiya Brain Core Integration** (Main AI processing)
- [ ] **Memory Systems Integration** (Short-term & Long-term memory)
- [ ] **Tool Layer Integration** (Local system actions, web lookup)
- [ ] **Response Formation Pipeline** (Context-based tone selection)
- [ ] **Expressive TTS Engine Integration** (Voice persona selection)

### 🔧 Technical Improvements
- [ ] Web interface integration
- [ ] Real-time streaming transcription
- [ ] Enhanced error handling
- [ ] Performance optimizations
- [ ] Additional language support
- [ ] Audio preprocessing improvements

## ⚠️ Known Issues

- 2 languages can intercept during conversation 
- Real-time recognition may have slight delays depending on system performance

## 🔧 Installation Troubleshooting

### PyAudio Installation Issues
If you encounter issues installing PyAudio:

**On macOS:**
```bash
brew install portaudio
pip install pyaudio
```

**On Ubuntu/Debian:**
```bash
sudo apt-get install portaudio19-dev python3-pyaudio
pip install pyaudio
```

**On Windows:**
```bash
pip install pipwin
pipwin install pyaudio
```

## 📁 Project Structure

```
Maiya/
├── speechrecogniation.py    # Main speech recognition module (gmtSpeechReco)
├── index.html              # Maiya AI System Architecture Diagram
├── README.md               # This file
└── requirements.txt        # Python dependencies
```

## 🤝 Contributing

This project is under development. Contributions and suggestions are welcome! Feel free to:

- Report bugs
- Suggest new features
- Improve documentation
- Add language support
- Optimize performance

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- [OpenAI Whisper](https://github.com/openai/whisper) for the amazing speech recognition engine
- The open-source community for continuous improvements

---

**Note**: This is a development version. Features and APIs may change as the project evolves.
