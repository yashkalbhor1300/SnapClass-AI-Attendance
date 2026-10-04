import io

import numpy as np
import streamlit as st

try:
    from resemblyzer import VoiceEncoder, preprocess_wav
except Exception:
    VoiceEncoder = None
    preprocess_wav = None

try:
    import librosa
except Exception:
    librosa = None


@st.cache_resource
def load_voice_encoder():

    if VoiceEncoder is None:
        raise RuntimeError(
            "Resemblyzer is not installed correctly."
        )

    return VoiceEncoder()


def get_voice_embedding(audio_bytes):

    try:

        if not audio_bytes:
            raise ValueError(
                "No audio data was received."
            )

        if librosa is None:
            raise RuntimeError(
                "Librosa is not installed correctly."
            )

        if preprocess_wav is None:
            raise RuntimeError(
                "Resemblyzer could not be loaded."
            )

        encoder = load_voice_encoder()

        audio, sr = librosa.load(
            io.BytesIO(audio_bytes),
            sr=16000,
            mono=True
        )

        if audio is None or len(audio) == 0:
            raise ValueError(
                "The recorded audio is empty."
            )

        wav = preprocess_wav(audio)

        if wav is None or len(wav) == 0:
            raise ValueError(
                "Could not preprocess the recorded audio."
            )

        embedding = encoder.embed_utterance(wav)

        if embedding is None:
            raise ValueError(
                "Voice encoder returned no embedding."
            )

        return embedding.tolist()

    except Exception as e:

        st.error(
            f"Voice recognition error: {type(e).__name__}: {e}"
        )

        return None


def identify_speaker(
    new_embedding,
    candidates_dict,
    threshold=0.65
):

    if new_embedding is None or not candidates_dict:
        return None, 0.0

    new_embedding = np.asarray(
        new_embedding,
        dtype=np.float32
    )

    best_sid = None
    best_score = -1.0

    for sid, stored_embedding in candidates_dict.items():

        if stored_embedding:

            stored_embedding = np.asarray(
                stored_embedding,
                dtype=np.float32
            )

            similarity = np.dot(
                new_embedding,
                stored_embedding
            )

            if similarity > best_score:

                best_score = similarity
                best_sid = sid

    if best_score >= threshold:
        return best_sid, best_score

    return None, best_score


def process_bulk_audio(
    audio_bytes,
    candidates_dict,
    threshold=0.65
):

    try:

        if not audio_bytes:
            raise ValueError(
                "No audio data was received."
            )

        if librosa is None:
            raise RuntimeError(
                "Librosa is not installed correctly."
            )

        if preprocess_wav is None:
            raise RuntimeError(
                "Resemblyzer could not be loaded."
            )

        encoder = load_voice_encoder()

        audio, sr = librosa.load(
            io.BytesIO(audio_bytes),
            sr=16000,
            mono=True
        )

        if audio is None or len(audio) == 0:
            raise ValueError(
                "The recorded audio is empty."
            )

        segments = librosa.effects.split(
            audio,
            top_db=30
        )

        identified_results = {}

        for start, end in segments:

            if (end - start) < sr * 0.5:
                continue

            segment_audio = audio[start:end]

            wav = preprocess_wav(
                segment_audio
            )

            embedding = encoder.embed_utterance(
                wav
            )

            sid, score = identify_speaker(
                embedding,
                candidates_dict,
                threshold
            )

            if sid:

                if (
                    sid not in identified_results
                    or score > identified_results[sid]
                ):

                    identified_results[sid] = score

        return identified_results

    except Exception as e:

        st.error(
            f"Bulk voice processing error: "
            f"{type(e).__name__}: {e}"
        )

        return {}