import sys
import wenet

wav_file = sys.argv[1]
decoder = wenet.Decoder(lang='chs')
ans = decoder.decode_wav(wav_file)
print(ans)