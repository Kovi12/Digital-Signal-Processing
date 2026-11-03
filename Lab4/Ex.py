import myDSP
fName = "guitar.wav"
x, fs=myDSP.readWav(fName)
#x=x[:fs,:]
#myDSP.playWav(x,fs)
#myDSP.plotInTime(x,fs)
#myDSP.plotInFrequency(x,fs)
myDSP.spectrogram(fName)
