# Questions and definitions

- **Malleability:** An encryption algorithm is malleable if it is possible to transform a ciphertext into another cyphertext which decrypts to a related plaintext. An undesired property, since this would allow an attacker to modify the content of a message. Given an encryption of a plaintext *m*, it is possible to generate another ciphertext which decrypts to *f(m)*, for a known function *f* without necessarily learning or knowing about *m*. So, you can take the ciphertext, compute a new message and it will still be converted back to an alright plaintext that can be understood. Even though this property is undesired, there are some schemes that are malleable by design. This means that this property is desired and seen as a feature, and these schemes are called homomorphic encryption schemes. 

- **Homomorphic encryption:** A homomoprhic encryption scheme allows calculations on the ciphertext without the need to decrypt it first, the secret key is therefore not needed to compute new messages. They are inherently malleable. 

- **Ciphertext indistinguishability:** A property of many encryption schemes. If a scheme is indistinguishable, an adversary will not be able to distinguish pairs of ciphertexts based on the message they encrypt. This means that the adversary should not have a higher chance to determine what the message is then if it were to just guess randomly. 

- **IND-CPA (Indistinguishability under chosen-plaintext attack):** This is a proof that it will not help to know the content of the message in plaintext to determine if the ciphertexts represent the plaintext. 

- **IND-CCA1 (Indistinguishability under chosen ciphertext attack):** 

- **IND-CCA2 (Indistinguishability under adaptive chosen ciphertext attack):** 


1. **Argue that El-Gamal is IND-CPA. You do not have to give a formal proof, but you should clearly argue for it (using the mathematical expressions defining El Gamal):** 
Let's say an adversary Alice wants to challenge Bob: 
- Bob generates her his pairs, k<sub>priv</sub> = x and k<sub>pub</sub> = (g, A), where A = g<sup>x</sup>. He sends his public key as well as the other key information to Alice. 
- Alice computes and sends two chosen plaintexts m<sub>0</sub> and m<sub>1</sub> to Bob. 
- Bob chooses b = {0, 1} at random, and sends a challenge ciphertext to Alice C = E(key<sub>pub</sub>, m<sub>b</sub>) to Alice.
- Alice is free to perform computations to try to gain information about which message it is. At last, it should compute an outbit if b is 0 or 1. 

In ElGamal, the ciphertext computed by Bob will be (c<sub>1</sub>, c<sub>2</sub>) = (g<sup>k</sup>, m<sub>b</sub> * A<sup>k</sup>) = (g<sup>k</sup>, m * g<sup>xk</sup>). k is a value chosen from the same range as x. From this point, you could get the value c<sup>'</sup> =  g<sup>xk</sub> by multiplying c<sub>2</sub> with the inverse of m<sub>0</sub> if b = 0. If this was the case, you now have (c<sup>'</sup>, g<sup>k</sub>, g<sup>x</sub>) and now needs to decide whether c<sup>'</sup> = g<sup>xk</sub>, given (g<sup>k</sub>, g<sup>x</sub>, c<sup>'</sup>). If the group G in which the values x and k was chosen from holds the DDH assumption, this means that (g<sup>ab</sub>, g<sup>a</sub>, g<sup>b</sub>) are computationally indistinguishable. And therefore, ElGamal is IND-CPA, since there are no way of knowing if Alice chose the correct value on b. 


2. **Show that El-Gamal is malleable:** An encryption algorithm is malleable if one can compute a new message without knowing the content of the message m that decrypts to f(m). In the ElGamal cryptosystem, a plaintext m is encrypted as E(m)=(g<sup>b</sup>}, m * A<sup>b</sup>), where (g,A) is the public key. Given such a ciphertext (c<sub>1</sub>,c<sub>2</sub>), an adversary can compute (c<sub>1</sub>, t * c<sub>2</sub>), which is a valid encryption of tm, for any t. In ElGamal (and in RSA), one can combine encryptions of m<sub>1</sub> and m<sub>2</sub> to obtain a valid encryption of their product m<sub>1</sub> * m<sub>2</sub>. A new message t * m was computed and will be interpreted as a correct message, and therefore ElGamal is malleable. We also know this since ElGamal is a homomorphic encryption scheme. 

Step-by-step:
 - Bob has two keys, k<sub>priv</sub> = x and k<sub>pub</sub> = (g, A), where A = g<sup>x</sup>.
 - If Alice wants to send him a message, she computes (c<sub>1</sub>, c<sub>2</sub>) = (g<sup>y</sup>, m * A<sup>y</sup>), where y is a value randomly chosen from the same range as x = {0,1,..,q-1}, where q is the order and is shared between the two parties.
 - Bob decrypts the message with his private key by:
 m = c<sub>1</sub><sup>-x</sup> * c<sub>2</sub>
 m = g<sup>y*-x</sup> * m * A<sup>y</sup>
 And since A = g<sup>x</sup>:
 m = g<sup>-xy</sup> * m * g<sup>xy</sup>
 m = m
 - An adversary could multiply c<sub>2</sub> with a valid value t and send it to Bob, which will lead to:
 t * c<sub>2</sub> = t * m * A<sup>y</sup>
 m = c<sub>1</sub><sup>-x</sup> * c<sub>2</sub>
 m = g<sup>y*-x</sup> * t * m * A<sup>y</sup>
 And since A = g<sup>x</sup>:
 m = g<sup>-xy</sup> * t * m * g<sup>xy</sup>
 m = t * m

3. **Show that El-Gamal is not IND-CCA2:** 
Let's say an adversary Alice wants to challenge Bob: 
- Bob generates her his pairs, k<sub>priv</sub> = x and k<sub>pub</sub> = (g, A), where A = g<sup>x</sup>. He sends his public key as well as the other key information to Alice. 
- Alice computes and sends two chosen plaintexts m<sub>0</sub> and m<sub>1</sub> to Bob. 
- Bob chooses b = {0, 1} at random, and sends a challenge ciphertext to Alice C = E(key<sub>pub</sub>, m<sub>b</sub>) to Alice.
- Alice is now able to send ciphertexts to a decryption oracle, which will decrypt any ciphertext except the challenge that was sent to Alice from Bob. This allows her to find out whether m<sub>0</sub> or m<sub>1</sub> was sent due to:
    - Alice can compute a new ciphertext with a new message: c<sub>new</sub> =(g<sup>k</sup>, A<sup>k</sup> * m<sub>b</sub> * m<sub>0</sub><sup>-1</sup> * m<sub>new</sub>)
    - She does this for both m<sub>0</sub> and m<sub>1</sub>, which one of them will compute c<sub>new</sub> =(g<sup>k</sup>, A<sup>k</sup> * m<sub>new</sub>)
    - She can send this to the decrypting oracle to confirm that it will decrypt to her new message. Hence, ElGamal is not IND-CCA2.