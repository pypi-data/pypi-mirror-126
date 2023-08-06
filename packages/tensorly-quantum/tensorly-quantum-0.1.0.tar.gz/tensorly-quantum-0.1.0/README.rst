================
TensorLy_Quantum
================


TensorLy-Quantum is a Python library for Tensor-Based Quantum Machine Learning that
builds on top of `TensorLy <https://github.com/tensorly/tensorly/>`_
and `PyTorch <https://pytorch.org/>`_.

- **Website:** http://tensorly.org/quantum/
- **Source-code:**  https://github.com/tensorly/quantum

With TensorLy-Quantum, you can easily: 

- **Create large quantum circuit**: Tensor network formalism requires up to exponentially less memory for quantum simulation than traditional vector and matrix approaches.
- **Leverage tensor methods**: the state vectors are efficiently represented in factorized form as Tensor-Rings (MPS) and the operators as TT-Matrices (MPO)
- **Efficient simulation**: tensorly-quantum leverages the factorized structure to efficiently perform quantum simulation without ever forming the full, dense operators and state-vectors
- **Multi-Basis Encoding**: we provide multi-basis encoding out-of-the-box for scalable experimentation
- **Solve hard problems**: we provide all the tools to solve the MaxCut problem for an unprecendented number of qubits / vertices


Installing TensorLy-Quantum
============================

Through pip
-----------

.. code:: 

   pip install tensorly-quantum
   
   
From source
-----------

.. code::

  git clone https://github.com/tensorly/quantum
  cd quantum
  pip install -e .
  
