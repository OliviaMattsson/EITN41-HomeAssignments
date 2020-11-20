Read about the property notions malleability, homomorphic encryption, IND-CPA, IND-CCA1 and IND-CCA2.

- **Malleability:** An encryption algorithm is malleable if it is possible to transform a ciphertext into another cyphertext which decrypts to a related plaintext. An undesired property, since this would allow an attacker to modify the content of a message. Given an encryption of a plaintext *m*, it is possible to generate another ciphertext which decrypts to *f(m)*, for a known function *f* without necessarily learning or knowing about *m*. So, you can take the ciphertext, compute a new message and it will still be converted back to an alright plaintext that can be understood. Even though this property is undesired, there are some schemes that are malleable by design. This means that this property is desired and seen as a feature, and these schemes are called homomorphic encryption schemes. 

- **Homomorphic encryption:** 

- **IND-CPA (Indistinguishability under chosen-plaintext attack):** 

- **IND-CCA1 (Indistinguishability under chosen ciphertext attack):** 

- **IND-CCA2 (Indistinguishability under adaptive chosen ciphertext attack):** 


1. Argue that El-Gamal is IND-CPA. You do not have to give a formal proof, but you should clearly argue for it (using the mathematical expressions defining El Gamal).


2. Show that El-Gamal is malleable.
    In the ElGamal cryptosystem, a plaintext m is encrypted as E(m)=(g<sup>b</sup>}, m * A<sup>b</sup>), where (g,A) is the public key. Given such a ciphertext (c<sub>1</sub>,c<sub>2</sub>), an adversary can compute (c<sub>1</sub>, t * c<sub>2</sub>), which is a valid encryption of tm, for any t. In ElGamal (and in RSA), one can combine encryptions of m<sub>1</sub> and m<sub>2</sub> to obtain a valid encryption of their product m<sub>1</sub> * m<sub>2</sub>.

3. Show that El-Gamal is not IND-CCA2.