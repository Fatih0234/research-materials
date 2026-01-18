## For the all-pay auction, we describe the auction format as follows:

648

649

650

651

652

653

654

655

656

657

658

659

660

661

662

663

664

665

666

667

668

669

670

671

672

673

674

675

676

677

678

679

680

681

682

683

684

685

686

687

688

689

690

691

692

693

694

695

696

697

698

699

700

701

- In this game, you will participate in an auction for a prize against {{num\_bidders}} other bidders. You will play this game for {{n}} rounds.
- At the start of each round, bidders will see their value for the prize, randomly drawn between $0 and ${{private}}, with all values equally likely.
- After learning your value, you will submit a bid privately at the same time as the other bidders. Bids must be between $0 and ${{private}} in ${{ increment}} increments.
- The highest bidder wins the prize. All bidders ( including the winner) pay their submitted bid. If you win, your earnings will increase by your value for the prize, and decrease by your bid. If you don't win, your earnings will still decrease by your bid.
- After each auction, we will display all bids and all bidders' profits. Ties for the highest bid will be resolved randomly.
