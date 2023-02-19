import torch


class HeadVer2:
    def __call__(self, x: torch.Tensor) -> torch.Tensor:
        """
        :param x: (B, T, C)
        :return: out (B, T, C)
        """
        # --- TODO 3 --- #\
        """
        1    0    0    0 
        0.5  0.5  0    0
        0.3  0.3  0.3  0
        0.25 0.25 0.25 0.25 
        """
        T = x.shape[1]
        wei = torch.tril(torch.ones(T, T)).to(x.device)
        wei = wei / wei.sum(1, keepdim=True)
        out = wei @ x
        # ------------ #
        return out
