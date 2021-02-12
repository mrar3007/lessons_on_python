from itertools import permutations as prm

print(
    '\n'.join(
        list(
            map(
                lambda s: ''.join(
                    list(
                        map(
                            str,
                            s
                        )
                    )
                ),
                prm(
                    range(
                        1,
                        int(input()) + 1)
                )
            )
        )
    )
)