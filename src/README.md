
# Instructions

## Before you run
To run the program, you need:

1.install following python packages if you don't have it:

- nltk: http://www.nltk.org/install.html
- scikit-learn: `pip3 install -U scikit-learn`
- scipy: `pip3 install -U scipy`
- tweepy: `pip3 install tweepy` http://docs.tweepy.org/en/v3.5.0/install.html

2.Get the dataset from http://cs.stanford.edu/people/alecmgo/trainingandtestdata.zip. 
And put them in the `/data/` directory rename them to: `test.csv` and `training.csv`

3.Change the first line of python interpreter to the one in your machine: `#! /usr/local/bin/python3`


## How to run it?

1.Grant execuation : `chmod +x ./demo1_training.py`

2.Steps

```bash
$ "Please give how many data you want to train: " 
$ # Give the number of dataset you want to train

$ "Please give the model you want to use to train (nb or svm) :" 
$ # input 'nb' or 'svm'
```

3.Sample output

```bash
./demo1_training.py
Please give how many data you want to train: 100
Please give the model you want to use to train (nb or svm) : nb
Processing tweets ...
Train on 80 data, Validate on 20 data using Naive Bayes Classifier...
Training complete.
Training time: 0.0518679999999998 secs
Validation Accuracy is : 0.6
Most Informative Features
           contains(day) = True              neg : pos    =      3.0 : 1.0
          contains(time) = True              neg : pos    =      1.8 : 1.0
         contains(laugh) = True              neg : pos    =      1.7 : 1.0
         contains(sleep) = True              neg : pos    =      1.7 : 1.0
           contains(not) = True              neg : pos    =      1.5 : 1.0
          contains(love) = True              pos : neg    =      1.4 : 1.0
         contains(going) = True              neg : pos    =      1.4 : 1.0
           contains(bed) = True              neg : pos    =      1.4 : 1.0
         contains(watch) = True              neg : pos    =      1.4 : 1.0
       contains(tonight) = False             neg : pos    =      1.1 : 1.0
       contains(twitter) = False             neg : pos    =      1.1 : 1.0
           contains(not) = False             pos : neg    =      1.1 : 1.0
           contains(day) = False             pos : neg    =      1.1 : 1.0
           contains(cry) = False             pos : neg    =      1.1 : 1.0
          contains(time) = False             pos : neg    =      1.1 : 1.0
Processing test tweets ...
Testing Accuracy is : 0.36
```

4. If you want to run demo2, please make sure you have the classifier in the /model directory.
If not, please first run train_classifier_ondisk.py, or it will not find the specific classifier.

```bash
$./train_classifier_ondisk.py
Please give how many data you want to train: 500
Please give the model you want to use to train (nb or svm) : svm
Processing tweets ...
Train on 400 data, Validate on 100 data using Support Vector Machine...
Training complete.
Training time: 0.7505410000000001 secs
Validation Accuracy is : 0.63
Tagging test data...
Testing Accuracy is : 0.6545961002785515

$./demo2_classify_live_tweets.py
Please give the model you want to use (nb or svm) : svm
Please give how many real time tweets you want to collect: 5
Collecting stream tweets ...
And Donald's playing the worst version of "man" too -- angry, ignorant, with bad clothes, manners, ethics, and hair. https://t.co/8vHHJznxBL
#GeorgeClooney #AmalClooney thanks for attempting to rig the election for Hillary. You LIED about where the $ goes. https://t.co/vQKwGAkAq4
@News_Liberal @cdmr9816 Then why is my FB page covered in NRA hate Hillary memes? Got some gun humping relatives!
RT @MardiLovejoy: @PoliticsPeach #Hillary is the most racist candidate in this election  @janewishon @AcUhuru @JoyAnnReid @CAS2328
RT @21damone: LATEST RASMUSSEN POLL
TRUMP: 41%
HILLARY: 39%
&amp; to think we haven't even started on her.......
Classify the tweets ...
========================================
And Donald's playing the worst version of "man" too -- angry, ignorant, with bad clothes, manners, ethics, and hair. https://t.co/8vHHJznxBL => neg
#GeorgeClooney #AmalClooney thanks for attempting to rig the election for Hillary. You LIED about where the $ goes. https://t.co/vQKwGAkAq4 => neg
@News_Liberal @cdmr9816 Then why is my FB page covered in NRA hate Hillary memes? Got some gun humping relatives! => neg
RT @MardiLovejoy: @PoliticsPeach #Hillary is the most racist candidate in this election  @janewishon @AcUhuru @JoyAnnReid @CAS2328 => neg
RT @21damone: LATEST RASMUSSEN POLL
TRUMP: 41%
HILLARY: 39%
&amp; to think we haven't even started on her....... => pos

```


